from flask import Flask, request, render_template
import requests

app = Flask(__name__)
PEXELS_API_KEY = "kRbY1KiT7jkPfS6p8b3XeDCmHUzPApZI0XdlnsTvCYjuF8j4mEqmpnMO"


def fetch_images(query):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=10"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return [photo['src']['medium'] for photo in data['photos']]
    return []


@app.route("/", methods=["GET", "POST"])
def home():
    images = []
    if request.method == "POST":
        query = request.form.get("query")
        images = fetch_images(query)
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run(debug=True)
