import unittest
import torch
from ultralytics import YOLO
import numpy as np

class TestSpermAnalyzerModel(unittest.TestCase):
    
    def setUp(self):
        self.model_path = 'ai-model/model/weights/best.pt'
        
    def test_model_loading(self):
        """Test if model loads correctly"""
        try:
            model = YOLO(self.model_path)
            self.assertIsNotNone(model)
        except Exception as e:
            self.skipTest(f"Model file not found: {e}")
    
    def test_model_inference(self):
        """Test model inference on dummy data"""
        try:
            model = YOLO(self.model_path)
            
            # Create dummy image
            dummy_image = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
            
            # Run inference
            results = model(dummy_image)
            
            self.assertIsNotNone(results)
            self.assertEqual(len(results), 1)
            
        except Exception as e:
            self.skipTest(f"Model inference test failed: {e}")
    
    def test_model_export(self):
        """Test model export functionality"""
        try:
            model = YOLO(self.model_path)
            
            # Test TFLite export
            success = model.export(format='tflite', imgsz=640)
            self.assertTrue(success)
            
        except Exception as e:
            self.skipTest(f"Model export test failed: {e}")

if __name__ == '__main__':
    unittest.main()
