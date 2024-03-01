# Face Detection Web App
This web application, built with Flask, allows users to perform face detection on uploaded images using a pre-trained machine learning model. The face detection model is designed to classify images into different facial expression categories.
<p align="center">
  <img src="https://i.ibb.co/Msj92ZN/Screenshot-2024-02-11-135748.png" alt="Alt text">
</p>

# Dataset Link🔗
https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection. 

# Ensure you have the required dependencies installed:

```bash
pip install flask pillow tensorflow
```
## Features

1. **Web Interface:**
   - Utilizes Flask for a user-friendly web-based interface.
2. **Upload and Detect:**
   - Allows users to upload an image and performs face detection using a pre-trained model.
3. **Labeling:**
   - Provides class labels for the detected faces.
# Customization
- Model Path: Replace "your_face_detection_model.h5" with the path to your face detection model file.
- Label Path: Replace "your_face_labels.txt" with the path to your face labels file.
- Upload Folder: Adjust the UPLOAD_FOLDER variable in app.py based on your preferences.

# Usage
1. Upload an image containing faces on the web app.
2. Click the "Detect Faces" button to perform face detection.
3. View the predicted facial expression class for the detected faces.
# Project Structure
* app.py: The main Flask application file containing route definitions and the face detection logic.
* uploads_faces: Folder to store user-uploaded images.

Feel free to explore and customize the project to suit your needs!

If you have any questions or encounter issues, please feel free to reach out. Happy face detecting! 😊
