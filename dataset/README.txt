# Dataset Folder

Place your training data here in the following structure:

```
dataset/
├── images/
│   ├── train/    ← put training images (.jpg/.png) here
│   └── val/      ← put validation images (.jpg/.png) here
└── labels/
    ├── train/    ← YOLO .txt label files for training images
    └── val/      ← YOLO .txt label files for validation images
```

## Where to get the dataset

Download from Kaggle:
https://www.kaggle.com/datasets/andrewmvd/face-mask-detection

The Kaggle dataset comes in Pascal VOC (XML) format.
You need to convert it to YOLO format first.

## Easy way — use Roboflow (recommended for beginners)

1. Go to https://roboflow.com and create a free account
2. Upload the Kaggle dataset
3. Export in "YOLOv8" format
4. Download and extract into this dataset/ folder

## Label format (YOLO .txt)

Each image needs a matching .txt file with the same name.
Each line in the .txt = one detected object:

  class_id  cx  cy  width  height

All values are normalized (0 to 1).

Class IDs:
  0 = with_mask
  1 = without_mask
  2 = mask_weared_incorrect

Example label file content:
  0 0.512 0.423 0.180 0.210
  1 0.750 0.380 0.160 0.195

## After placing data, run training

```bash
python train_yolo.py
```

The best model will be saved to model/best.pt automatically.
