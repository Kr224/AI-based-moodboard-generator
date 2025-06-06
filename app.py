from flask import Flask, request, render_template
import requests
from ml_filter import filter_images  # Import ML filtering function

app = Flask(__name__)
PEXELS_API_KEY = "kRbY1KiT7jkPfS6p8b3XeDCmHUzPApZI0XdlnsTvCYjuF8j4mEqmpnMO"

def fetch_images(query):
    """Fetch images from Pexels based on user query"""
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=15"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers)

    print("API Response Code:", response.status_code)  # Debugging line
    print("Raw API Response:", response.json())  # Debugging line

    if response.status_code == 200:
        data = response.json()
        return [photo['src']['large'] for photo in data['photos']]
    return []

@app.route("/", methods=["GET", "POST"])
def home():
    images = []
    if request.method == "POST":
        query = request.form.get("query")
        raw_images = fetch_images(query)  # Get images from Pexels

        # Apply AI filtering for relevance
        images = filter_images(raw_images, query)

    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
