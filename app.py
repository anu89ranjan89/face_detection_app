import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Page Config
st.set_page_config(
    page_title="Face Detection App",
    page_icon="😀",
    layout="wide"
)

st.title("😀 AI Face Detection App")

st.markdown("""
Upload an image and detect human faces using OpenCV Haar Cascades.
""")

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Upload Image
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# Detect Faces
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    gray = cv2.cvtColor(
        image_np,
        cv2.COLOR_RGB2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            image_np,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    st.success(
        f"Faces Detected: {len(faces)}"
    )

    st.image(
        image_np,
        caption="Detected Faces",
        use_container_width=True
    )

st.divider()

st.subheader("About")

st.write(
    "This project uses OpenCV Haar Cascade Classifier to detect human faces in uploaded images."
)