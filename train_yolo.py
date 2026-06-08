from ultralytics import YOLO
import pathlib
import shutil

def main():
    BASE_DIR = pathlib.Path(__file__).parent
    model = YOLO("yolov8m.pt")
    model.train(
        data=str(BASE_DIR / "data.yaml"),
        epochs=20,
        imgsz=640,
        device=0,
        batch=16,
        workers=0
    )
    
    # Automatically copy the trained model to model/best.pt
    best_weights = BASE_DIR / "runs" / "detect" / "train" / "weights" / "best.pt"
    if best_weights.exists():
        (BASE_DIR / "model").mkdir(exist_ok=True)
        shutil.copy(str(best_weights), str(BASE_DIR / "model" / "best.pt"))
        print("\nTraining complete! model/best.pt has been successfully saved.")

if __name__ == "__main__":
    main()