#!/usr/bin/env python3
"""
Sperm Analyzer AI - YOLOv8 Training Script
"""

import os
from ultralytics import YOLO
import torch
from pathlib import Path

def setup_training():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    os.makedirs('runs/train', exist_ok=True)
    os.makedirs('model/weights', exist_ok=True)
    
    return device

def train_model():
    print("Starting Sperm Analyzer AI Training...")
    
    device = setup_training()
    
    model = YOLO('yolov8n.pt')
    
    results = model.train(
        data='data/dataset.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        name='sperm_analyzer',
        device=device,
        patience=10,
        save=True,
        save_period=10,
        val=True,
        plots=True,
        verbose=True
    )
    
    model.export(format='tflite')
    model.export(format='onnx')
    
    print("Training completed!")
    return results

if __name__ == "__main__":
    train_model()
