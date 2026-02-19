import os
import numpy as np
import cv2
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import matplotlib.pyplot as plt
import io
import base64

# Get the folder where this app.py file lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the static folder if it does not exist
STATIC_DIR = os.path.join(BASE_DIR, "static")
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

app = Flask(__name__)

# Locate the model in the parent directory (workspace root) or current directory.
# This handles running the script from the `hematovision` folder.
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "Blood Cell.h5"))
# Fallback: check same folder as app.py too
if not os.path.exists(MODEL_PATH):
    alt = os.path.abspath(os.path.join(BASE_DIR, "Blood Cell.h5"))
    if os.path.exists(alt):
        MODEL_PATH = alt

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found. Expected 'Blood Cell.h5' at: {MODEL_PATH}\n"
        f"Place the model file in the project root (one level above this folder) or next to app.py"
    )

try:
    model = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model at {MODEL_PATH}: {e}") from e
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']


def predict_image_class(image_path, model):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_preprocessed = preprocess_input(img_resized.reshape((1, 224, 224, 3)))
    predictions = model.predict(img_preprocessed)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_idx]
    return predicted_class_label, img_rgb


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            file_path = os.path.join(STATIC_DIR, file.filename)
            file.save(file_path)
            predicted_class_label, img_rgb = predict_image_class(file_path, model)

            # Convert image to string for displaying in HTML
            _, img_encoded = cv2.imencode('.png', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
            img_str = base64.b64encode(img_encoded).decode('utf-8')

            return render_template("result.html", class_label=predicted_class_label, img_data=img_str)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
