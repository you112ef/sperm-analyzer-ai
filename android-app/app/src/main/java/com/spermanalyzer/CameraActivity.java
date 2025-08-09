package com.spermanalyzer;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.Preview;
import androidx.camera.lifecycle.ProcessCameraProvider;
import androidx.camera.view.PreviewView;

public class CameraActivity extends AppCompatActivity {
    
    private PreviewView previewView;
    private Button captureButton;
    private ImageCapture imageCapture;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
        
        previewView = findViewById(R.id.preview_view);
        captureButton = findViewById(R.id.btn_capture);
        
        captureButton.setOnClickListener(v -> captureImage());
        
        startCamera();
    }
    
    private void startCamera() {
        // Camera initialization code here
        Toast.makeText(this, "Camera starting...", Toast.LENGTH_SHORT).show();
    }
    
    private void captureImage() {
        // Image capture code here
        Toast.makeText(this, "Image captured!", Toast.LENGTH_SHORT).show();
    }
}
