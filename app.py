from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

app = Flask(__name__)

# Set up the upload folder for storing the user-uploaded images
UPLOAD_FOLDER = 'uploads_faces'  # Adjusted for face detection
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the pre-trained machine learning model for face detection
MODEL_PATH = "your_face_detection_model.h5"  # Replace with your face detection model
if not os.path.exists(MODEL_PATH):
    print(f"Model file '{MODEL_PATH}' not found.")
    exit()
face_detection_model = load_model(MODEL_PATH)

# Load the class labels from a text file
LABEL_PATH = 'your_face_labels.txt'  # Replace with your face labels file
if not os.path.exists(LABEL_PATH):
    print(f"Label file '{LABEL_PATH}' not found.")
    exit()
class_labels_faces = [line.strip() for line in open(LABEL_PATH)]

def preprocess_face_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjusted for face detection
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

@app.route('/')
def index():
    return render_template('index_faces.html')  # Adjusted for face detection

@app.route('/detect_faces', methods=['POST'])  # Adjusted endpoint for face detection
def detect_faces():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file chosen'}), 400

    try:
        img_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(img_path)

        # Preprocess the face image
        processed_face_image = preprocess_face_image(img_path)

        # Perform face detection using the model
        face_prediction = face_detection_model.predict(processed_face_image)

        # Get the predicted class label for faces
        predicted_face_class = np.argmax(face_prediction)
        predicted_face_label = class_labels_faces[predicted_face_class]

        # If predicted_face_label is not one of the labels, it's probably an error
        if predicted_face_label not in class_labels_faces:
            return jsonify({'error': 'Face detection failed'}), 500

        response = {'detected_face_class': predicted_face_label}
        return jsonify(response), 200

    except Exception as e:
        error_message = f"An error occurred while processing the face image: {str(e)}"
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
