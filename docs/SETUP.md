# Setup Guide for Sperm Analyzer AI

## Prerequisites

1. Python 3.8+
2. Android Studio
3. Git

## AI Model Setup

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Prepare your dataset in the `ai-model/data/` directory

5. Run training:
   ```bash
   cd ai-model
   python train.py
   ```

## Android App Setup

1. Open Android Studio
2. Open the `android-app` directory as a project
3. Sync project with Gradle files
4. Copy the trained model (`.tflite` file) to `android-app/app/src/main/assets/`
5. Build and run the app

## Dataset Format

The dataset should follow YOLO format:
- Images in `images/` folder
- Labels in `labels/` folder
- Each label file should contain: `class_id center_x center_y width height`

## Model Export

To export the trained model for Android:
```bash
python ai-model/scripts/export_model.py --model model/weights/best.pt --format tflite
```
