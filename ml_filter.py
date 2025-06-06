import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from sklearn.cluster import KMeans

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights="imagenet")


def preprocess_img(img_url):
    """Download and preprocess an image for ML filtering"""
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((224, 224))  # Resize to model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array


def classify_image(img_url):
    """Use AI to classify the image content"""
    img_array = preprocess_img(img_url)
    preds = model.predict(img_array)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]
    return decoded_preds


def filter_images(image_urls, user_query):
    """Filter images using AI classification and keyword matching, allowing broader matches."""
    relevant_images = []

    # Broaden search using synonyms
    synonyms = {
        "vampire": ["blood", "dark", "gothic", "red_wine", "fangs", "mask", "wig", "Halloween", "creepy"],
        "beach": ["ocean", "waves", "sand", "swim", "sunset", "surfing"]
    }

    expanded_query = user_query.split()
    if user_query in synonyms:
        expanded_query += synonyms[user_query]  # Add related words

    for img_url in image_urls:
        predictions = classify_image(img_url)
        labels = [label[1] for label in predictions]  # Extract labels
        print(f"Image Labels: {labels}")  # Debugging output

        # Allow broader matches (if any label contains ANY expanded keyword)
        if any(keyword.lower() in label.lower() or label.lower() in keyword.lower() for label in labels for keyword in
               expanded_query):
            relevant_images.append(img_url)
            print(f"✅ Kept: {img_url}")
        else:
            print(f"❌ Removed: {img_url}")

    # If filtering removed everything, **return original images instead**
    if not relevant_images:
        print("⚠️ No AI-filtered results, returning unfiltered images instead.")
        return image_urls

    return relevant_images
