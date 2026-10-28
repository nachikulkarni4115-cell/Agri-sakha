import json
import logging
import os
import secrets

from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    session,
    redirect,
    url_for,
    abort
)

try:
    # Optional: load variables from a local .env file during development.
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import tensorflow as tf

from services.prediction_service import (
    InvalidImageError,
    load_image,
    load_preprocessor,
    predict_image,
    occlusion_overlay
)
from services.disease_service import (
    get_disease_info,
    count_conditions,
    SUPPORTED_LANGUAGES
)


logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

log = logging.getLogger("agrisakha")


# ============================================================
# Configuration (all overridable with environment variables)
# ============================================================

def env_flag(name, default=False):
    value = os.environ.get(name)

    if value is None:
        return default

    return value.strip().lower() in {"1", "true", "yes", "on"}


DEBUG = env_flag("FLASK_DEBUG")

MAX_UPLOAD_MB = float(os.environ.get("MAX_UPLOAD_MB", "8"))

# Below this confidence the app refuses to name a disease and asks for a better photo.
CONFIDENCE_THRESHOLD = float(os.environ.get("CONFIDENCE_THRESHOLD", "0.60"))

# Build the "what the AI looked at" heatmap (adds ~50 quick forward passes per request).
EXPLAIN_ENABLED = env_flag("AGRISAKHA_EXPLAIN", True)


# ============================================================
# Flask Application
# ============================================================

app = Flask(__name__)

secret_key = os.environ.get("SECRET_KEY")

if not secret_key:
    secret_key = secrets.token_hex(32)

    log.warning(
        "SECRET_KEY is not set. Using a random key: language choices will reset "
        "whenever the server restarts, and will NOT work across multiple gunicorn "
        "workers. Set SECRET_KEY in your environment for production."
    )

app.secret_key = secret_key

app.config.update(
    MAX_CONTENT_LENGTH=int(MAX_UPLOAD_MB * 1024 * 1024),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=env_flag("SESSION_COOKIE_SECURE", False),
    JSON_AS_ASCII=False
)


# ============================================================
# Base Directories
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_DIR = os.environ.get(
    "AGRISAKHA_MODEL_DIR",
    os.path.join(BASE_DIR, "models")
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "AgriSakha_MobileNetV2.keras"
)

CLASS_NAMES_PATH = os.path.join(
    MODEL_DIR,
    "class_names.json"
)

PREPROCESSING_PATH = os.path.join(
    MODEL_DIR,
    "preprocessing_spec.json"
)

TRANSLATIONS_DIR = os.path.join(
    BASE_DIR,
    "translations"
)


# ============================================================
# Load ML Model, Class Names and Preprocessing Spec
# ============================================================

def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


log.info("Loading AgriSakha ML model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

log.info("ML model loaded successfully.")


class_names = read_json(CLASS_NAMES_PATH)["class_names"]

log.info("Loaded %d classes.", len(class_names))


# The preprocessing spec is now actually used to prepare every image.
preprocessor = load_preprocessor(
    read_json(PREPROCESSING_PATH)
)

log.info("Preprocessing: %r", preprocessor)


# ============================================================
# Translations (loaded once, not on every request)
# ============================================================

def load_all_translations():
    loaded = {}

    for code in SUPPORTED_LANGUAGES:
        path = os.path.join(TRANSLATIONS_DIR, f"{code}.json")

        if os.path.exists(path):
            loaded[code] = read_json(path)

    # English is the fallback for any missing language file.
    fallback = loaded.get("en", {})

    for code in SUPPORTED_LANGUAGES:
        loaded.setdefault(code, fallback)

    return loaded


TRANSLATIONS = load_all_translations()


def current_language():
    language = session.get("language", "en")

    if language not in SUPPORTED_LANGUAGES:
        return "en"

    return language


# ============================================================
# Security Headers
# ============================================================

@app.after_request
def add_security_headers(response):

    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "same-origin")
    response.headers.setdefault("Permissions-Policy", "camera=(self), microphone=()")

    if request.path == "/predict":
        response.headers["Cache-Control"] = "no-store"

    return response


# ============================================================
# Home Route
# ============================================================

@app.route("/")
def home():

    language = session.get("language")

    # No language chosen yet: show the language selection screen.
    if language not in SUPPORTED_LANGUAGES:

        return render_template(
            "language.html"
        )

    translations = TRANSLATIONS[language]

    return render_template(
        "index.html",
        language=language,
        translations=translations,
        stats={
            "crops": len(translations.get("crops", [])),
            "conditions": count_conditions(),
            "languages": len(SUPPORTED_LANGUAGES)
        }
    )


# ============================================================
# Set Language Route
# Used by the language screen AND the navbar language switcher.
# ============================================================

@app.route(
    "/set-language",
    methods=["POST"]
)
def set_language():

    language = request.form.get(
        "language"
    )

    if language in SUPPORTED_LANGUAGES:
        session["language"] = language

    return redirect(
        url_for("home")
    )


# ============================================================
# Reset Language Route (development only)
# ============================================================

@app.route(
    "/reset-language"
)
def reset_language():

    if not app.debug:
        abort(404)

    session.pop(
        "language",
        None
    )

    return redirect(
        url_for("home")
    )


# ============================================================
# Health Check (for AWS load balancers / uptime checks)
# ============================================================

@app.route("/health")
def health():

    return jsonify({
        "status": "ok",
        "classes": len(class_names)
    })


# ============================================================
# Error Handlers
# ============================================================

@app.errorhandler(413)
def file_too_large(_error):

    t = TRANSLATIONS[current_language()]

    return jsonify({
        "success": False,
        "error": t.get("err_too_large", "This image is too large.")
    }), 413


# ============================================================
# Prediction Route
# ============================================================

def error_response(key, fallback, status):

    t = TRANSLATIONS[current_language()]

    return jsonify({
        "success": False,
        "error": t.get(key, fallback)
    }), status


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    language = current_language()


    # --------------------------------------------------------
    # Check Image Upload
    # --------------------------------------------------------

    upload = request.files.get("image")

    if upload is None or not upload.filename:

        return error_response(
            "err_no_image",
            "Please select an image first.",
            400
        )


    # --------------------------------------------------------
    # Decode + validate the image in memory.
    # Nothing is written to disk, so there is no file name to
    # abuse (path traversal) and no leftovers to clean up.
    # --------------------------------------------------------

    try:
        image = load_image(upload.stream)

    except InvalidImageError:

        return error_response(
            "err_invalid_image",
            "This file is not a valid image.",
            400
        )


    # --------------------------------------------------------
    # Run Prediction
    # --------------------------------------------------------

    try:

        top = predict_image(
            model,
            class_names,
            image,
            preprocessor,
            top_k=3
        )

        best_class, best_confidence = top[0]

        candidates = []

        for class_name, probability in top:

            info = get_disease_info(class_name, language)

            candidates.append({
                "key": info["key"],
                "crop": info["crop"],
                "disease": info["disease"],
                "confidence": round(probability * 100, 1)
            })


        # ----------------------------------------------------
        # Low confidence: do not guess. Ask for a better photo.
        # ----------------------------------------------------

        if best_confidence < CONFIDENCE_THRESHOLD:

            return jsonify({
                "success": True,
                "status": "uncertain",
                "threshold": round(CONFIDENCE_THRESHOLD * 100),
                "candidates": candidates
            })


        # ----------------------------------------------------
        # Confident result
        # ----------------------------------------------------

        disease_info = get_disease_info(
            best_class,
            language
        )

        heatmap = None

        if EXPLAIN_ENABLED:

            heatmap = occlusion_overlay(
                model,
                class_names,
                preprocessor,
                image,
                best_class
            )

        return jsonify({

            "success": True,

            "status": "ok",

            "prediction": {

                "crop": disease_info["crop"],

                "disease": disease_info["disease"],

                "confidence": round(
                    best_confidence * 100,
                    1
                ),

                "risk": disease_info["risk"]

            },

            "candidates": candidates,

            "information": {

                "symptoms": disease_info["symptoms"],

                "prevention": disease_info["prevention"],

                "next_steps": disease_info["next_steps"]

            },

            "heatmap": heatmap

        })


    # --------------------------------------------------------
    # Handle Prediction Errors
    # The real error goes to the log, never to the user.
    # --------------------------------------------------------

    except Exception:

        log.exception("Prediction failed")

        return error_response(
            "err_server",
            "Something went wrong while analysing the photo.",
            500
        )


# ============================================================
# Run Application
# ============================================================

if __name__ == "__main__":

    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=DEBUG
    )
