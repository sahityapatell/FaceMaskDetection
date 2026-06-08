import os
import pathlib
import cv2
from flask import Flask, render_template, Response, request, jsonify, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO

# ── App setup ──────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "mask_detection_secret_key"

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR      = pathlib.Path(__file__).parent
MODEL_PATH    = BASE_DIR / "model" / "best.pt"
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
OUTPUT_FOLDER = BASE_DIR / "static" / "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ── Load model once ────────────────────────────────────────────────────────────
model = YOLO(str(MODEL_PATH))

# ── Allowed extensions ─────────────────────────────────────────────────────────
ALLOWED_IMAGES = {"jpg", "jpeg", "png", "webp", "bmp"}
ALLOWED_VIDEOS = {"mp4", "avi", "mov", "mkv"}

def allowed(filename, allowed_set):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_set

# ── Webcam stream generator ────────────────────────────────────────────────────
def generate_frames():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            results = model(frame, conf=0.5, verbose=False)
            for r in results:
                frame = r.plot()

            ret, buffer = cv2.imencode(".jpg", frame)
            if not ret:
                continue

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
    finally:
        cap.release()

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/detect/image", methods=["POST"])
def detect_image():
    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected.")
        return redirect(url_for("index"))

    if not allowed(file.filename, ALLOWED_IMAGES):
        flash("Invalid file type. Please upload a JPG, PNG, WEBP, or BMP image.")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    in_path  = UPLOAD_FOLDER / filename
    out_path = OUTPUT_FOLDER / filename

    file.save(str(in_path))

    try:
        results = model(str(in_path))
        for r in results:
            cv2.imwrite(str(out_path), r.plot())
    except Exception as e:
        flash(f"Detection failed: {e}")
        return redirect(url_for("index"))

    return render_template("index.html", image="outputs/" + filename)


@app.route("/detect/video", methods=["POST"])
def detect_video():
    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected.")
        return redirect(url_for("index"))

    if not allowed(file.filename, ALLOWED_VIDEOS):
        flash("Invalid file type. Please upload a MP4, AVI, MOV, or MKV video.")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    in_path  = UPLOAD_FOLDER / filename
    out_name = "out_" + filename
    out_path = OUTPUT_FOLDER / out_name

    file.save(str(in_path))

    cap = cv2.VideoCapture(str(in_path))
    if not cap.isOpened():
        flash("Could not open video file.")
        return redirect(url_for("index"))

    fps    = int(cap.get(cv2.CAP_PROP_FPS)) or 25
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter(
        str(out_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps, (width, height)
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, verbose=False)
        for r in results:
            writer.write(r.plot())

    cap.release()
    writer.release()

    return render_template("index.html", video="outputs/" + out_name)


@app.route("/download/<filename>")
def download(filename):
    path = OUTPUT_FOLDER / filename
    if not path.exists():
        flash("File not found.")
        return redirect(url_for("index"))
    return send_file(str(path), as_attachment=True)


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=False)