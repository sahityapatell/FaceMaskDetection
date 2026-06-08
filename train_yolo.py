"""
train_yolo.py — Train YOLOv8 on the face mask dataset.

Usage:
    python train_yolo.py

The trained model is saved automatically by YOLO under runs/detect/train/weights/.
Copy best.pt to model/best.pt after training.
"""

from ultralytics import YOLO
import os

# ── Config ────────────────────────────────────────────────────────────────────
DATA_YAML = 'data.yaml'   # Path to dataset config
MODEL_BASE = 'yolov8n.pt' # Base model: n=nano, s=small, m=medium
EPOCHS = 50
IMAGE_SIZE = 640
BATCH_SIZE = 16
PROJECT_DIR = 'runs'
# ─────────────────────────────────────────────────────────────────────────────


def train():
    print("Loading base model...")
    model = YOLO(MODEL_BASE)

    print(f"Starting training for {EPOCHS} epochs...")
    results = model.train(
        data=DATA_YAML,
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        project=PROJECT_DIR,
        name='face_mask_detection',
        exist_ok=True,
        verbose=True
    )

    best_weights = os.path.join(PROJECT_DIR, 'face_mask_detection', 'weights', 'best.pt')
    if os.path.exists(best_weights):
        os.makedirs('model', exist_ok=True)
        import shutil
        shutil.copy(best_weights, 'model/best.pt')
        print("\n Training complete! model/best.pt is ready.")
    else:
        print(f"\n Training done. Copy weights manually from: {best_weights}")


if __name__ == '__main__':
    train()
