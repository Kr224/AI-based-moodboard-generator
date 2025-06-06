# 🌟 MoodBoardAI – AI-Powered Moodboard Generator

## 🖼️ Overview
MoodBoardAI is a simple AI-based moodboard generator that fetches relevant images based on user input and filters them using **machine learning** for improved accuracy.  
Inspired by Pinterest, this project helps users quickly visualize moods, aesthetics, and concepts.

## 🚀 Features
- 🎨 **AI-Based Filtering** – Uses ML models to enhance search accuracy.
- 🏞 **Image Grid Layout** – Displays moodboards in a Pinterest-style grid.
- 🌙 **Dark Mode Toggle** – Easily switch between light and dark themes.
- 🔍 **Search-Based Image Fetching** – Pulls images dynamically using the Pexels API.
- ⚡ **Fast & Responsive** – Built with Flask and styled using CSS & JavaScript.

## 📦 Tech Stack
- **Frontend:** HTML, CSS (Grid Layout, Dark Mode)
- **Backend:** Flask (Python)
- **Machine Learning:** TensorFlow (MobileNetV2), scikit-learn
- **Image Fetching:** Pexels API

## 🔧 Installation & Setup

### Clone this repository:
```bash
git clone https://github.com/your-username/MoodBoardAI.git
cd MoodBoardAI
```

### Install dependencies:
````bash
pip install flask requests tensorflow scikit-learn numpy pillow
````

### Add your Pexels API key in app.py:
````bash
PEXELS_API_KEY = "your_api_key_here"
````

### Run the Flask app:
````bash
python app.py
````

### Open your browser and visit:
````bash
http://127.0.0.1:5000/
````

### 🖥️ Project Structure:

MoodBoardAI/
├── app.py              # Flask backend
├── ml_filter.py        # AI-based image filtering
├── static/
│   ├── style.css       # Custom styling
├── templates/
│   ├── index.html      # Frontend UI
├── README.md           # Documentation


