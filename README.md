# 🎭 Face Mask Detection System

A real-time face mask detection web application built with **YOLOv8**, **Flask**, and **OpenCV**. Detects whether people are wearing masks correctly, incorrectly, or not at all — across images, videos, and live webcam streams.

🌐 **Live Demo**: https://facemaskdetection-rcyk.onrender.com
> Note: Live demo may take ~50 seconds to load on first visit (free tier cold start). For full performance including webcam, run locally.

---

## 📸 Screenshots

| Home Page | Image Detection |
|-----------|----------------|
| ![home](static/screenshots/home_page.png) | ![image](static/screenshots/image_detection.png) |

---

## ✨ Features

- **Image Detection** — Upload JPG, PNG, WEBP, or BMP. Get annotated results with bounding boxes and confidence scores
- **Video Detection** — Process MP4, AVI, MOV, MKV files frame-by-frame. Download the annotated output
- **Live Webcam** — Real-time detection streamed to browser via MJPEG *(local only)*
- **Download Results** — Save processed images and videos directly from the browser

### Detection Classes
| Class | Description |
|-------|-------------|
| `with_mask` | Mask worn correctly |
| `without_mask` | No mask worn |
| `mask_weared_incorrect` | Mask worn incorrectly (nose/mouth exposed) |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | YOLOv8 (Ultralytics) |
| Backend | Python, Flask |
| Computer Vision | OpenCV |
| Frontend | HTML5, CSS3, Vanilla JavaScript |

---

## 📁 Folder Structure

```
FaceMaskDetection/
│
├── app.py                  # Flask backend (all routes)
├── train_yolo.py           # YOLOv8 training script
├── data.yaml               # Dataset config for YOLO training
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── best.pt             # Trained YOLOv8 weights (not in git)
│
├── templates/
│   └── index.html          # Single-page frontend
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   ├── uploads/            # Temp input files
│   ├── outputs/            # Processed results
│   └── screenshots/
│
└── dataset/                # Training data (not in git)
    ├── images/train/
    ├── images/val/
    ├── labels/train/
    └── labels/val/
```

---

## 🚀 Installation & Setup

### Data Sets
* **Recommended Kaggle Dataset**: [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection) for training YOLOv8 models.

### Prerequisites
* Python 3.9+
* Web Browser (Chrome, Firefox, Safari, Edge, etc.)
* NVIDIA GPU (Optional, for optimized AI inference speed)

### 1. Clone the repository
```bash
git clone https://github.com/sahityapatell/FaceMaskDetection.git
cd FaceMaskDetection
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the trained model
Download `best.pt` from the link below and place it at `model/best.pt`:
```
https://drive.google.com/file/d/19hGNgffmV2edri_74WZNMT6gT5nht2aO/view?usp=drive_link
```

### 5. Run the app
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🏋️ Training Your Own Model

If you want to train the model from scratch on your own dataset:
1. Organize your dataset folders(read README.txt in dataset folder) in YOLO format:
   ```text
   dataset/
       ├── images/
   │   ├── train/
   │   └── val/
       └── labels/
       ├── train/
       └── val/
   ```
2. Ensure your dataset path is correctly configured in `data.yaml`.
3. Run the training script:
   ```bash
   python train_yolo.py
   ```
4. The best weights are automatically copied to `model/best.pt` upon training completion.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

Developed by [@sahityapatell](https://github.com/sahityapatell)