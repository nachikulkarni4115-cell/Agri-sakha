"""
AgriSakha - Prediction Service

Responsibilities
    * Validate and decode an uploaded image (in memory, nothing is written to disk)
    * Preprocess it exactly the way the model was trained (driven by preprocessing_spec.json)
    * Return the top-k predictions
    * Optionally build an "attention" heatmap (occlusion sensitivity) so the user can
      see which part of the leaf influenced the result. It is model-agnostic, so it
      works with any Keras classifier without knowing its internal layer names.
"""

import base64
import io
import json
import logging
import os
import re

import numpy as np
from PIL import Image, ImageFilter, ImageOps

log = logging.getLogger("agrisakha.prediction")

# Decompression-bomb guard: refuse absurdly large images instead of exhausting memory.
Image.MAX_IMAGE_PIXELS = 50_000_000

ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}
DEFAULT_SIZE = (224, 224)


class InvalidImageError(ValueError):
    """The uploaded file is not a usable JPG / PNG / WEBP image."""


# ------------------------------------------------------------
# Preprocessing
# ------------------------------------------------------------

class Preprocessor:
    """
    Turns a PIL image into the array the model expects.

    mode
        "unit"       pixels scaled to 0..1        (x / 255)
        "symmetric"  pixels scaled to -1..1       (MobileNetV2 preprocess_input)
        "raw"        pixels left at 0..255        (model rescales internally)
    """

    def __init__(self, size=DEFAULT_SIZE, mode="unit", reason="default"):
        self.size = tuple(size)
        self.mode = mode
        self.reason = reason

    def array(self, image):
        resized = image.resize(self.size)
        data = np.asarray(resized, dtype="float32")

        if self.mode == "symmetric":
            return data / 127.5 - 1.0
        if self.mode == "raw":
            return data
        return data / 255.0

    def batch(self, image):
        return np.expand_dims(self.array(image), axis=0)

    def __repr__(self):
        return f"Preprocessor(size={self.size}, mode={self.mode!r}, reason={self.reason!r})"


def _find_size(spec):
    for key in ("input_size", "image_size", "target_size", "img_size", "size"):
        value = spec.get(key)

        if isinstance(value, int) and value > 0:
            return (value, value)

        if isinstance(value, (list, tuple)) and len(value) >= 2:
            try:
                return (int(value[0]), int(value[1]))
            except (TypeError, ValueError):
                continue

    return DEFAULT_SIZE


def _find_mode(spec):
    """
    Work out the pixel scaling from preprocessing_spec.json.

    The spec format is not fixed, so this reads the whole file as text and looks for
    well-known markers. The decision is logged at startup; if it is wrong, override
    it with AGRISAKHA_PREPROCESS=unit|symmetric|raw.
    """
    override = os.environ.get("AGRISAKHA_PREPROCESS", "").strip().lower()

    if override in {"unit", "symmetric", "raw"}:
        return override, "AGRISAKHA_PREPROCESS override"

    text = json.dumps(spec).lower()

    symmetric_markers = ("preprocess_input", "mobilenet", "127.5", "symmetric", "minus_one")

    # Matches ranges written like "[-1, 1]", "-1 to 1" or "-1..1", but not a stray -1.
    minus_one_to_one = re.search(
        r"(?<![\d.])-1(?:\.0)?\s*(?:,|to|\.\.|and)\s*\+?1(?:\.0)?\b", text
    )

    if any(marker in text for marker in symmetric_markers) or minus_one_to_one:
        return "symmetric", "spec mentions MobileNet / -1..1 scaling"

    if any(marker in text for marker in ("255", "0-1", "[0, 1]", "unit", "rescale")):
        return "unit", "spec mentions 0..1 scaling"

    if any(marker in text for marker in ("raw", "none", "no_scaling")):
        return "raw", "spec says no external scaling"

    return "unit", "spec had no scaling hint, using 0..1 (the previous behaviour)"


def load_preprocessor(spec):
    spec = spec if isinstance(spec, dict) else {}

    size = _find_size(spec)
    mode, reason = _find_mode(spec)

    preprocessor = Preprocessor(size=size, mode=mode, reason=reason)

    log.info("Using %r", preprocessor)

    return preprocessor


# ------------------------------------------------------------
# Image loading
# ------------------------------------------------------------

def load_image(source):
    """
    Decode an uploaded file (path or file-like object) into an RGB PIL image.
    Validates the real image format, not the file name.
    """
    try:
        image = Image.open(source)
        image.load()  # force a full decode so truncated files fail here
    except Exception as exc:
        raise InvalidImageError("Could not read image.") from exc

    if image.format not in ALLOWED_FORMATS:
        raise InvalidImageError(f"Unsupported image format: {image.format}")

    # Phones store rotation in EXIF; without this, portrait photos arrive sideways.
    image = ImageOps.exif_transpose(image)

    return image.convert("RGB")


# ------------------------------------------------------------
# Prediction
# ------------------------------------------------------------

def _as_probabilities(raw):
    """Accept either softmax probabilities or raw logits."""
    values = np.asarray(raw, dtype="float64")

    looks_like_probabilities = (
        values.min() >= 0.0 and abs(values.sum() - 1.0) < 0.01
    )

    if looks_like_probabilities:
        return values

    shifted = values - values.max()
    exp = np.exp(shifted)

    return exp / exp.sum()


def predict_image(model, class_names, image, preprocessor, top_k=3):
    """
    Returns a list of (class_name, probability) sorted best-first.
    The first item is the model's prediction.
    """
    batch = preprocessor.batch(image)

    raw = model.predict(batch, verbose=0)[0]

    probabilities = _as_probabilities(raw)

    top_k = max(1, min(top_k, len(class_names)))

    order = np.argsort(probabilities)[::-1][:top_k]

    return [
        (class_names[int(index)], float(probabilities[int(index)]))
        for index in order
    ]


# ------------------------------------------------------------
# Explanation heatmap (occlusion sensitivity)
# ------------------------------------------------------------

def _occlusion_grid(model, class_names, preprocessor, image, target_class, steps=7):
    """
    Slide a neutral patch across the leaf and measure how much the model's
    confidence in `target_class` drops. A big drop means that region mattered.
    """
    base = preprocessor.array(image)
    height, width = base.shape[:2]

    patch_h = max(8, height // 4)
    patch_w = max(8, width // 4)

    ys = np.linspace(0, height - patch_h, steps).astype(int)
    xs = np.linspace(0, width - patch_w, steps).astype(int)

    neutral = base.mean(axis=(0, 1), keepdims=True)

    batch = [base]

    for y in ys:
        for x in xs:
            occluded = base.copy()
            occluded[y:y + patch_h, x:x + patch_w, :] = neutral
            batch.append(occluded)

    predictions = model.predict(np.stack(batch), verbose=0)

    target_index = class_names.index(target_class)

    scores = np.array(
        [_as_probabilities(row)[target_index] for row in predictions]
    )

    baseline = scores[0]

    drops = np.clip(baseline - scores[1:], 0.0, None).reshape(steps, steps)

    peak = drops.max()

    if peak < 1e-4:
        return None

    return drops / peak


def _colorize(heat):
    """Map 0..1 heat to RGB + alpha (green -> yellow -> red)."""
    stops = np.array([0.0, 0.35, 0.65, 1.0])

    red = np.interp(heat, stops, [20, 34, 250, 239])
    green = np.interp(heat, stops, [30, 197, 204, 68])
    blue = np.interp(heat, stops, [80, 94, 21, 68])
    alpha = np.interp(heat, stops, [0.0, 0.28, 0.52, 0.78])

    return np.stack([red, green, blue], axis=-1), alpha[..., None]


def occlusion_overlay(model, class_names, preprocessor, image, target_class, max_side=420):
    """
    Returns a base64 JPEG data URL of the leaf with the attention heatmap blended
    on top, or None if no meaningful map could be produced.
    """
    try:
        grid = _occlusion_grid(model, class_names, preprocessor, image, target_class)

        if grid is None:
            return None

        scale = max_side / max(image.size)
        size = (max(1, int(image.width * scale)), max(1, int(image.height * scale)))

        base = image.resize(size)

        heat_image = Image.fromarray((grid * 255).astype("uint8"), mode="L")
        heat_image = heat_image.resize(size, Image.BICUBIC)
        heat_image = heat_image.filter(ImageFilter.GaussianBlur(radius=max(size) / 60))

        heat = np.asarray(heat_image, dtype="float32") / 255.0

        peak = heat.max()
        if peak > 0:
            heat = heat / peak

        color, alpha = _colorize(heat)

        blended = np.asarray(base, dtype="float32") * (1 - alpha) + color * alpha

        output = Image.fromarray(np.clip(blended, 0, 255).astype("uint8"))

        buffer = io.BytesIO()
        output.save(buffer, format="JPEG", quality=82)

        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")

        return f"data:image/jpeg;base64,{encoded}"

    except Exception:
        # The heatmap is a bonus feature: never let it break a prediction.
        log.exception("Could not build the attention heatmap")
        return None
