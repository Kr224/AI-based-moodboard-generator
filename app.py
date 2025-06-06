from flask import Flask, request, render_template
import requests
from ml_filter import filter_images  # Import ML filtering function

app = Flask(__name__)
UNSPLASH_ACCESS_KEY = "VYcgHmM7cl-YP2jYMvbe2DVcqbL3YA65UCE-VOW_KNw"

def fetch_images(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}&per_page=15"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [photo['urls']['regular'] for photo in data['results']]
    return []


@app.route("/", methods=["GET", "POST"])
def home():
    images = []
    if request.method == "POST":
        query = request.form.get("query")
        raw_images = fetch_images(query)

        # Apply AI filtering for relevance
        images = filter_images(raw_images, query)

    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
