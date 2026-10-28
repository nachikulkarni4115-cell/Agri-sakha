// ==================================================
// AgriSakha — Frontend
// Dependency-free: spring-style motion, scroll reveals,
// pointer effects, photo compression, scan animation,
// results, voice output and local scan history.
// ==================================================

(function () {

    "use strict";


    // --------------------------------------------------
    // Shared helpers
    // --------------------------------------------------

    var translations = window.AGRISAKHA_TRANSLATIONS || {};
    var language = window.AGRISAKHA_LANGUAGE || "en";

    var reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    var finePointer = window.matchMedia(
        "(hover: hover) and (pointer: fine)"
    ).matches;

    function $(selector, root) {
        return (root || document).querySelector(selector);
    }

    function $$(selector, root) {
        return Array.prototype.slice.call(
            (root || document).querySelectorAll(selector)
        );
    }

    function t(key, fallback) {
        return translations[key] || fallback || "";
    }

    function wait(ms) {
        return new Promise(function (resolve) {
            window.setTimeout(resolve, ms);
        });
    }

    function clamp(value, min, max) {
        return Math.max(min, Math.min(max, value));
    }

    function storageGet(key) {
        try {
            return window.localStorage.getItem(key);
        } catch (error) {
            return null;
        }
    }

    function storageSet(key, value) {
        try {
            window.localStorage.setItem(key, value);
        } catch (error) { /* storage blocked: ignore */ }
    }

    function formatPercent(value) {
        return (Number.isInteger(value) ? value : value.toFixed(1)) + "%";
    }


    // --------------------------------------------------
    // Theme toggle (dark <-> light)
    // --------------------------------------------------

    var themeToggle = $("#themeToggle");

    if (themeToggle) {

        themeToggle.addEventListener("click", function () {

            var root = document.documentElement;

            var next = root.getAttribute("data-theme") === "light"
                ? "dark"
                : "light";

            root.setAttribute("data-theme", next);

            storageSet("agrisakha-theme", next);

            var meta = $('meta[name="theme-color"]');

            if (meta) {
                meta.setAttribute("content", next === "light" ? "#f3f0e6" : "#060d09");
            }
        });
    }


    // --------------------------------------------------
    // Scroll: progress bar + navbar state
    // --------------------------------------------------

    var navWrap = $(".nav-wrap");
    var progressBar = $(".scroll-progress");
    var scrollTicking = false;

    function updateScroll() {

        scrollTicking = false;

        var max = document.documentElement.scrollHeight - window.innerHeight;
        var ratio = max > 0 ? window.scrollY / max : 0;

        if (progressBar) {
            progressBar.style.setProperty("--progress", ratio.toFixed(4));
        }

        if (navWrap) {
            navWrap.classList.toggle("scrolled", window.scrollY > 24);
        }
    }

    window.addEventListener("scroll", function () {

        if (!scrollTicking) {
            scrollTicking = true;
            window.requestAnimationFrame(updateScroll);
        }

    }, { passive: true });

    updateScroll();


    // --------------------------------------------------
    // Reveal on scroll (staggered by data-delay)
    // --------------------------------------------------

    function initReveal() {

        var items = $$(".reveal");

        if (!items.length) {
            return;
        }

        function finish(element) {

            // After the entrance finishes, drop the reveal classes so they never
            // interfere with hover / tilt transforms.
            var done = false;

            function cleanup() {

                if (done) {
                    return;
                }

                done = true;

                element.classList.remove("reveal", "is-visible");
                element.style.removeProperty("--d");
            }

            element.addEventListener("transitionend", function (event) {

                if (event.propertyName === "opacity") {
                    cleanup();
                }
            });

            window.setTimeout(cleanup, 1800);
        }

        items.forEach(function (element) {

            element.style.setProperty("--d", element.getAttribute("data-delay") || "0");
        });

        if (reduceMotion || !("IntersectionObserver" in window)) {

            items.forEach(function (element) {
                element.classList.add("is-visible");
            });

            return;
        }

        var observer = new IntersectionObserver(function (entries) {

            entries.forEach(function (entry) {

                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("is-visible");

                finish(entry.target);

                observer.unobserve(entry.target);
            });

        }, {
            threshold: 0.12,
            rootMargin: "0px 0px -40px 0px"
        });

        items.forEach(function (element) {
            observer.observe(element);
        });
    }


    // --------------------------------------------------
    // Count-up numbers (hero stats)
    // --------------------------------------------------

    function animateCount(element, target, options) {

        options = options || {};

        var duration = options.duration || 900;
        var decimals = options.decimals;
        var suffix = options.suffix || "";

        function format(value) {

            if (decimals === undefined) {
                return formatPercent(value).replace("%", "") + suffix;
            }

            return value.toFixed(decimals) + suffix;
        }

        if (reduceMotion) {
            element.textContent = format(target);
            return;
        }

        var start = performance.now();

        function tick(now) {

            var progress = Math.min(1, (now - start) / duration);

            // ease-out expo
            var eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);

            element.textContent = format(target * eased);

            if (progress < 1) {
                window.requestAnimationFrame(tick);
            } else {
                element.textContent = format(target);
            }
        }

        window.requestAnimationFrame(tick);
    }

    function initStats() {

        var stats = $(".stats");

        if (!stats || reduceMotion || !("IntersectionObserver" in window)) {
            return;
        }

        var observer = new IntersectionObserver(function (entries) {

            entries.forEach(function (entry) {

                if (!entry.isIntersecting) {
                    return;
                }

                $$("[data-count]", stats).forEach(function (element) {

                    var target = Number(element.getAttribute("data-count")) || 0;

                    animateCount(
                        element,
                        target,
                        { decimals: 0, duration: 1400 }
                    );
                });

                observer.disconnect();
            });
        });

        observer.observe(stats);
    }


    // --------------------------------------------------
    // Pointer effects: spotlight, tilt, magnetic, parallax
    // --------------------------------------------------

    function initSpotlight() {

        if (!finePointer) {
            return;
        }

        $$(".spot").forEach(function (element) {

            element.addEventListener("pointermove", function (event) {

                var rect = element.getBoundingClientRect();

                element.style.setProperty("--mx", (event.clientX - rect.left) + "px");
                element.style.setProperty("--my", (event.clientY - rect.top) + "px");
            });
        });
    }

    function initTilt() {

        if (!finePointer || reduceMotion) {
            return;
        }

        $$(".tilt").forEach(function (tile) {

            tile.addEventListener("pointermove", function (event) {

                var rect = tile.getBoundingClientRect();

                var x = (event.clientX - rect.left) / rect.width - 0.5;
                var y = (event.clientY - rect.top) / rect.height - 0.5;

                tile.style.transition = "border-color 0.3s ease, box-shadow 0.3s ease";

                tile.style.transform =
                    "perspective(800px) rotateX(" + (-y * 6).toFixed(2) + "deg) " +
                    "rotateY(" + (x * 6).toFixed(2) + "deg) translateY(-3px)";
            });

            tile.addEventListener("pointerleave", function () {

                tile.style.transition = "";
                tile.style.transform = "";
            });
        });
    }

    function initMagnetic() {

        if (!finePointer || reduceMotion) {
            return;
        }

        $$(".magnetic").forEach(function (element) {

            element.addEventListener("pointermove", function (event) {

                if (element.disabled) {
                    return;
                }

                var rect = element.getBoundingClientRect();

                var dx = event.clientX - (rect.left + rect.width / 2);
                var dy = event.clientY - (rect.top + rect.height / 2);

                element.style.transition = "box-shadow 0.3s ease, background 0.3s ease, opacity 0.3s ease";

                element.style.transform =
                    "translate(" + (dx * 0.22).toFixed(1) + "px, " + (dy * 0.32).toFixed(1) + "px)";
            });

            element.addEventListener("pointerleave", function () {

                // Back to rest on a spring curve (defined in CSS .btn).
                element.style.transition = "";
                element.style.transform = "";
            });
        });
    }

    function initHeroParallax() {

        var hero = $("#hero");
        var visual = $(".hero-visual");

        if (!hero || !visual || !finePointer || reduceMotion) {
            return;
        }

        $$(".float-chip", visual).forEach(function (chip) {
            chip.style.setProperty("--depth", chip.getAttribute("data-depth") || "0");
        });

        var targetX = 0;
        var targetY = 0;
        var currentX = 0;
        var currentY = 0;
        var running = false;

        function loop() {

            // Critically-damped-ish follow: smooth, no overshoot.
            currentX += (targetX - currentX) * 0.09;
            currentY += (targetY - currentY) * 0.09;

            visual.style.setProperty("--px", currentX.toFixed(3));
            visual.style.setProperty("--py", currentY.toFixed(3));

            var settled =
                Math.abs(targetX - currentX) < 0.001 &&
                Math.abs(targetY - currentY) < 0.001;

            if (settled) {
                running = false;
                return;
            }

            window.requestAnimationFrame(loop);
        }

        function kick() {

            if (!running) {
                running = true;
                window.requestAnimationFrame(loop);
            }
        }

        hero.addEventListener("pointermove", function (event) {

            var rect = hero.getBoundingClientRect();

            targetX = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
            targetY = ((event.clientY - rect.top) / rect.height - 0.5) * 2;

            kick();
        });

        hero.addEventListener("pointerleave", function () {

            targetX = 0;
            targetY = 0;

            kick();
        });
    }


    initReveal();
    initStats();
    initSpotlight();
    initTilt();
    initMagnetic();
    initHeroParallax();


    // ==================================================
    // ANALYZE STUDIO
    // ==================================================

    var uploadArea = $("#uploadArea");

    // Not on this page (e.g. the language screen): nothing more to wire up.
    if (!uploadArea) {
        return;
    }

    var galleryInput = $("#imageInput");
    var cameraInput = $("#cameraInput");

    var previewContainer = $("#previewContainer");
    var frame = $("#frame");
    var imagePreview = $("#imagePreview");
    var previewMeta = $("#previewMeta");
    var removeImageButton = $("#removeImageButton");

    var predictButton = $("#predictButton");
    var predictButtonText = $("#predictButtonText");
    var predictIcon = $("#predictIcon");
    var loadingSpinner = $("#loadingSpinner");
    var statusMessage = $("#statusMessage");

    var resultPanel = $("#resultPanel");
    var resultEmpty = $("#resultEmpty");
    var resultSection = $("#resultSection");
    var uncertainSection = $("#uncertainSection");

    var resultCrop = $("#resultCrop");
    var resultDisease = $("#resultDisease");
    var resultConfidence = $("#resultConfidence");
    var confidenceRingValue = $("#confidenceRingValue");
    var riskBlock = $("#riskBlock");
    var riskText = $("#riskText");
    var matchList = $("#matchList");
    var uncertainList = $("#uncertainList");

    var explainBlock = $("#explainBlock");
    var heatImage = $("#heatImage");
    var heatToggle = $("#heatToggle");

    var resultSymptoms = $("#resultSymptoms");
    var resultPrevention = $("#resultPrevention");
    var resultNextSteps = $("#resultNextSteps");

    var listenButton = $("#listenButton");
    var listenText = $("#listenText");
    var listenIcon = $("#listenIcon");

    var analyzeAnotherButton = $("#analyzeAnotherButton");
    var retryButton = $("#retryButton");

    var recentBlock = $("#recentBlock");
    var recentList = $("#recentList");
    var recentClear = $("#recentClear");

    var GAUGE_CIRCUMFERENCE = 2 * Math.PI * 52;

    var MAX_RAW_BYTES = 30 * 1024 * 1024;   // refuse absurd originals before decoding
    var MAX_UPLOAD_BYTES = 8 * 1024 * 1024; // matches the server default
    var MAX_SIDE = 1280;

    var state = {
        original: null,
        prepared: null,
        previewUrl: null,
        heatmapUrl: null,
        speechText: "",
        busy: false
    };


    // --------------------------------------------------
    // Status helpers
    // --------------------------------------------------

    function showStatus(message, type) {

        statusMessage.textContent = message;

        statusMessage.className = "status-message" + (type ? " " + type : "");
    }

    function clearStatus() {
        showStatus("", "");
    }


    // --------------------------------------------------
    // Right-hand panel switching
    // --------------------------------------------------

    function replayStagger(container) {

        $$(":scope > *", container).forEach(function (child, index) {
            child.style.setProperty("--n", String(index));
        });

        container.classList.remove("is-in");

        // Force reflow so the entrance animation restarts.
        void container.offsetWidth;

        container.classList.add("is-in");
    }

    function showPanel(which) {

        resultEmpty.classList.toggle("hidden", which !== "empty");
        resultSection.classList.toggle("hidden", which !== "result");
        uncertainSection.classList.toggle("hidden", which !== "uncertain");

        if (which === "result") {
            replayStagger(resultSection);
        }

        if (which === "uncertain") {
            replayStagger(uncertainSection);
        }
    }


    // --------------------------------------------------
    // Image preparation: decode + resize + compress
    // (phone photos are 3-10 MB; farmers are often on slow networks)
    // --------------------------------------------------

    function decodeImage(file) {

        return new Promise(function (resolve, reject) {

            var url = URL.createObjectURL(file);
            var image = new Image();

            image.onload = function () {
                URL.revokeObjectURL(url);
                resolve(image);
            };

            image.onerror = function () {
                URL.revokeObjectURL(url);
                reject(new Error("decode"));
            };

            image.src = url;
        });
    }

    function canvasToBlob(canvas, quality) {

        return new Promise(function (resolve) {
            canvas.toBlob(resolve, "image/jpeg", quality);
        });
    }

    async function prepareImage(file) {

        var allowedTypes = ["image/jpeg", "image/png", "image/webp"];
        var canSendOriginal = allowedTypes.indexOf(file.type) !== -1 && file.size <= MAX_UPLOAD_BYTES;

        var image;

        try {
            image = await decodeImage(file);
        } catch (error) {

            // The browser cannot decode it. Send the original only if the server can.
            if (canSendOriginal) {
                return file;
            }

            throw error;
        }

        var scale = Math.min(1, MAX_SIDE / Math.max(image.naturalWidth, image.naturalHeight));

        // Small JPEGs are already fine as they are.
        if (scale === 1 && file.type === "image/jpeg" && file.size < 1.2 * 1024 * 1024) {
            return file;
        }

        var canvas = document.createElement("canvas");

        canvas.width = Math.max(1, Math.round(image.naturalWidth * scale));
        canvas.height = Math.max(1, Math.round(image.naturalHeight * scale));

        canvas.getContext("2d").drawImage(image, 0, 0, canvas.width, canvas.height);

        var blob = await canvasToBlob(canvas, 0.88);

        if (!blob) {
            return canSendOriginal ? file : Promise.reject(new Error("encode"));
        }

        // Never make a file bigger.
        if (canSendOriginal && blob.size >= file.size) {
            return file;
        }

        return new File([blob], "leaf.jpg", { type: "image/jpeg" });
    }


    // --------------------------------------------------
    // Selecting / removing an image
    // --------------------------------------------------

    async function handleSelectedImage(file) {

        if (state.busy || !file) {
            return;
        }

        if (!file.type || file.type.indexOf("image/") !== 0) {

            showStatus(t("err_invalid_image", "Please choose an image file."), "error");
            return;
        }

        if (file.size > MAX_RAW_BYTES) {

            showStatus(t("err_too_large", "This image is too large."), "error");
            return;
        }

        clearStatus();

        var prepared;

        try {
            prepared = await prepareImage(file);
        } catch (error) {

            showStatus(t("err_invalid_image", "This file is not a valid image."), "error");
            return;
        }

        if (prepared.size > MAX_UPLOAD_BYTES) {

            showStatus(t("err_too_large", "This image is too large."), "error");
            return;
        }

        releasePreviewUrl();

        state.original = file;
        state.prepared = prepared;
        state.previewUrl = URL.createObjectURL(prepared);

        imagePreview.src = state.previewUrl;

        var sizeKB = Math.max(1, Math.round(prepared.size / 1024));

        previewMeta.textContent = (file.name || "photo") + " · " + sizeKB + " KB";

        previewContainer.classList.remove("hidden");
        uploadArea.classList.add("hidden");

        predictButton.disabled = false;

        showPanel("empty");
        stopSpeaking();
    }

    function releasePreviewUrl() {

        if (state.previewUrl) {
            URL.revokeObjectURL(state.previewUrl);
            state.previewUrl = null;
        }
    }

    function removeSelectedImage() {

        state.original = null;
        state.prepared = null;
        state.heatmapUrl = null;

        releasePreviewUrl();

        galleryInput.value = "";
        cameraInput.value = "";

        imagePreview.removeAttribute("src");

        previewContainer.classList.add("hidden");
        uploadArea.classList.remove("hidden");

        frame.classList.remove("is-scanning");

        predictButton.disabled = true;

        showPanel("empty");
        clearStatus();
        stopSpeaking();
    }

    [galleryInput, cameraInput].forEach(function (input) {

        input.addEventListener("change", function () {

            var file = input.files && input.files[0];

            if (file) {
                handleSelectedImage(file);
            }
        });
    });

    removeImageButton.addEventListener("click", removeSelectedImage);


    // --------------------------------------------------
    // Drag & drop (works on the whole input column) + paste
    // --------------------------------------------------

    var dropTarget = $(".studio-input");

    ["dragenter", "dragover"].forEach(function (name) {

        dropTarget.addEventListener(name, function (event) {

            event.preventDefault();

            uploadArea.classList.add("dragover");
        });
    });

    ["dragleave", "drop"].forEach(function (name) {

        dropTarget.addEventListener(name, function (event) {

            event.preventDefault();

            uploadArea.classList.remove("dragover");
        });
    });

    dropTarget.addEventListener("drop", function (event) {

        var file = event.dataTransfer && event.dataTransfer.files && event.dataTransfer.files[0];

        if (file) {
            handleSelectedImage(file);
        }
    });

    document.addEventListener("paste", function (event) {

        var files = event.clipboardData && event.clipboardData.files;

        if (!files || !files.length) {
            return;
        }

        var image = Array.prototype.find.call(files, function (file) {
            return file.type.indexOf("image/") === 0;
        });

        if (image) {
            handleSelectedImage(image);
        }
    });


    // --------------------------------------------------
    // Predict
    // --------------------------------------------------

    function setBusy(isBusy) {

        state.busy = isBusy;

        predictButton.disabled = isBusy || !state.prepared;

        predictButtonText.textContent = isBusy
            ? t("loading", "Analyzing image...")
            : t("predict", "Predict Crop Health");

        predictIcon.classList.toggle("hidden", isBusy);
        loadingSpinner.classList.toggle("hidden", !isBusy);

        frame.classList.toggle("is-scanning", isBusy);
    }

    function ApiError(message) {
        this.userMessage = message;
    }

    async function predictCrop() {

        if (state.busy) {
            return;
        }

        if (!state.prepared) {

            showStatus(t("err_no_image", "Please select an image first."), "error");
            return;
        }

        setBusy(true);
        clearStatus();
        stopSpeaking();

        var startedAt = performance.now();

        try {

            var formData = new FormData();

            formData.append("image", state.prepared, state.prepared.name || "leaf.jpg");

            var response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            var data = null;

            try {
                data = await response.json();
            } catch (parseError) { /* handled below */ }

            if (!response.ok || !data || !data.success) {

                throw new ApiError(
                    (data && data.error) || t("err_server", "Unable to analyze the image.")
                );
            }

            // Keep the scan animation on screen long enough to read as a deliberate step
            // (and to avoid a flash when the server answers instantly).
            var elapsed = performance.now() - startedAt;

            if (!reduceMotion) {
                await wait(Math.max(0, 1300 - elapsed));
            }

            setBusy(false);

            if (data.status === "uncertain") {
                renderUncertain(data);
            } else {
                renderResult(data);
            }

        } catch (error) {

            setBusy(false);

            if (error instanceof ApiError) {

                showStatus(error.userMessage, "error");

            } else {

                console.error("Prediction error:", error);

                // fetch() itself rejecting means the network failed.
                showStatus(
                    error instanceof TypeError
                        ? t("err_network", "Couldn't reach the server.")
                        : t("err_server", "Unable to analyze the image."),
                    "error"
                );
            }
        }
    }

    predictButton.addEventListener("click", predictCrop);


    // --------------------------------------------------
    // Rendering
    // --------------------------------------------------

    function renderMatches(listElement, candidates) {

        listElement.textContent = "";

        (candidates || []).forEach(function (candidate, index) {

            var item = document.createElement("li");

            if (index === 0) {
                item.className = "is-first";
            }

            var row = document.createElement("div");
            row.className = "m-row";

            var name = document.createElement("span");
            name.textContent = candidate.crop + " · " + candidate.disease;

            var percent = document.createElement("b");
            percent.textContent = formatPercent(Number(candidate.confidence) || 0);

            row.appendChild(name);
            row.appendChild(percent);

            var bar = document.createElement("div");
            bar.className = "bar";

            var fill = document.createElement("i");
            fill.style.setProperty(
                "--w",
                clamp(Number(candidate.confidence) || 0, 0, 100) + "%"
            );

            bar.appendChild(fill);

            item.appendChild(row);
            item.appendChild(bar);

            listElement.appendChild(item);
        });
    }

    function setGauge(confidence) {

        var offset = GAUGE_CIRCUMFERENCE * (1 - confidence / 100);

        confidenceRingValue.style.transition = "none";
        confidenceRingValue.style.strokeDashoffset = String(GAUGE_CIRCUMFERENCE);

        void confidenceRingValue.getBoundingClientRect();

        window.requestAnimationFrame(function () {

            confidenceRingValue.style.transition = "";
            confidenceRingValue.style.strokeDashoffset = String(offset);
        });
    }

    function renderResult(data) {

        var prediction = data.prediction;
        var information = data.information;

        var confidence = clamp(Number(prediction.confidence) || 0, 0, 100);

        resultCrop.textContent = prediction.crop;
        resultDisease.textContent = prediction.disease;

        resultSymptoms.textContent = information.symptoms;
        resultPrevention.textContent = information.prevention;
        resultNextSteps.textContent = information.next_steps;

        var level = prediction.risk || "unknown";

        riskBlock.setAttribute("data-level", level);
        riskText.textContent = t("risk_" + level, t("risk_unknown", "Unknown"));

        renderMatches(matchList, data.candidates);

        // Heatmap (what the AI looked at)
        if (data.heatmap) {

            state.heatmapUrl = data.heatmap;

            heatToggle.checked = true;
            heatImage.src = data.heatmap;

            explainBlock.classList.remove("hidden");

        } else {

            state.heatmapUrl = null;
            explainBlock.classList.add("hidden");
        }

        showPanel("result");

        // Gauge and number animate after the panel is visible.
        setGauge(confidence);

        animateCount(resultConfidence, confidence, {
            decimals: Number.isInteger(confidence) ? 0 : 1,
            suffix: "%",
            duration: 1000
        });

        // Voice output
        state.speechText = [
            prediction.crop + ". " + prediction.disease + ".",
            information.symptoms,
            information.prevention,
            information.next_steps
        ].join(" ");

        saveRecent({
            crop: prediction.crop,
            disease: prediction.disease,
            confidence: confidence,
            risk: level,
            ts: Date.now()
        });

        revealPanelOnSmallScreens();
    }

    function renderUncertain(data) {

        renderMatches(uncertainList, data.candidates);

        showPanel("uncertain");

        revealPanelOnSmallScreens();
    }

    function revealPanelOnSmallScreens() {

        if (window.matchMedia("(max-width: 1000px)").matches) {

            resultPanel.scrollIntoView({
                behavior: reduceMotion ? "auto" : "smooth",
                block: "start"
            });
        }
    }

    heatToggle.addEventListener("change", function () {

        if (!state.heatmapUrl) {
            return;
        }

        heatImage.src = heatToggle.checked ? state.heatmapUrl : state.previewUrl;
    });


    // --------------------------------------------------
    // Analyze another / retry
    // --------------------------------------------------

    function startOver() {

        removeSelectedImage();

        $("#analyze").scrollIntoView({
            behavior: reduceMotion ? "auto" : "smooth",
            block: "start"
        });
    }

    analyzeAnotherButton.addEventListener("click", startOver);
    retryButton.addEventListener("click", startOver);


    // --------------------------------------------------
    // Voice output (Web Speech API)
    // --------------------------------------------------

    var speechSupported = "speechSynthesis" in window && "SpeechSynthesisUtterance" in window;

    var SPEECH_LANG = { en: "en-IN", hi: "hi-IN", mr: "mr-IN" };

    function setListening(isListening) {

        listenText.textContent = isListening
            ? t("stop_listening", "Stop")
            : t("listen", "Listen");

        listenIcon.querySelector("use").setAttribute(
            "href",
            isListening ? "#i-stop" : "#i-speaker"
        );
    }

    function stopSpeaking() {

        if (speechSupported) {
            window.speechSynthesis.cancel();
            setListening(false);
        }
    }

    function findVoice(tag) {

        var voices = window.speechSynthesis.getVoices();
        var wanted = tag.toLowerCase();
        var base = wanted.split("-")[0];

        function normalized(voice) {
            return voice.lang.replace("_", "-").toLowerCase();
        }

        return (
            voices.find(function (voice) { return normalized(voice) === wanted; }) ||
            voices.find(function (voice) { return normalized(voice).indexOf(base) === 0; }) ||
            null
        );
    }

    function toggleSpeaking() {

        var synth = window.speechSynthesis;

        if (synth.speaking) {
            stopSpeaking();
            return;
        }

        var tag = SPEECH_LANG[language] || "en-IN";

        var utterance = new SpeechSynthesisUtterance(state.speechText);

        utterance.rate = 0.95;
        utterance.lang = tag;

        var voice = findVoice(tag);

        // Many devices have a Hindi voice but no Marathi one; both use Devanagari.
        if (!voice && language === "mr") {
            voice = findVoice("hi-IN");
        }

        if (voice) {
            utterance.voice = voice;
            utterance.lang = voice.lang;
        }

        utterance.onend = utterance.onerror = function () {
            setListening(false);
        };

        synth.speak(utterance);

        setListening(true);
    }

    if (speechSupported) {

        listenButton.classList.remove("hidden");

        listenButton.addEventListener("click", toggleSpeaking);

        // Some browsers load voices asynchronously.
        window.speechSynthesis.getVoices();

        window.addEventListener("beforeunload", stopSpeaking);
    }


    // --------------------------------------------------
    // Recent scans (stored on this device only)
    // --------------------------------------------------

    var RECENT_KEY = "agrisakha-recent";
    var RECENT_MAX = 4;

    function loadRecent() {

        try {

            var parsed = JSON.parse(storageGet(RECENT_KEY) || "[]");

            return Array.isArray(parsed) ? parsed : [];

        } catch (error) {
            return [];
        }
    }

    function saveRecent(entry) {

        var list = loadRecent();

        list.unshift(entry);

        storageSet(RECENT_KEY, JSON.stringify(list.slice(0, RECENT_MAX)));

        renderRecent();
    }

    function renderRecent() {

        var list = loadRecent();

        recentList.textContent = "";

        recentBlock.classList.toggle("hidden", list.length === 0);

        var locale = { en: "en-IN", hi: "hi-IN", mr: "mr-IN" }[language] || "en-IN";

        list.forEach(function (entry) {

            var item = document.createElement("li");

            var label = document.createElement("span");

            label.textContent = entry.crop + " · " + entry.disease;

            var when = document.createElement("small");

            when.textContent = new Date(entry.ts).toLocaleDateString(locale, {
                day: "numeric",
                month: "short"
            });

            label.appendChild(when);

            var percent = document.createElement("b");

            percent.textContent = formatPercent(Number(entry.confidence) || 0);

            item.appendChild(label);
            item.appendChild(percent);

            recentList.appendChild(item);
        });
    }

    recentClear.addEventListener("click", function () {

        storageSet(RECENT_KEY, "[]");

        renderRecent();
    });

    renderRecent();

})();
