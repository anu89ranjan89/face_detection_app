# 😀 Face Detection App

## Overview

This project detects human faces in uploaded images using OpenCV's Haar Cascade Classifier.

The application allows users to upload images, automatically detects faces, draws bounding boxes around detected faces, and displays the total number of faces found.

## Features

* Upload JPG, JPEG, or PNG images
* Detect single or multiple faces
* Draw bounding boxes around faces
* Display face count
* Interactive Streamlit web interface

## Tech Stack

* Python
* OpenCV
* NumPy
* Pillow
* Streamlit

## Working

1. Upload an image.
2. Convert image to grayscale.
3. Apply Haar Cascade face detector.
4. Draw rectangles around detected faces.
5. Display results with face count.

## Project Structure

Face-Detection-App/

├── app.py

├── face_detection.py

├── haarcascade_frontalface_default.xml

├── requirements.txt

├── README.md

└── screenshots/


## Future Improvements

* Real-time webcam detection
* Face recognition
* Emotion detection
* Age and gender prediction

## Author

Anupriya Ranjan
