"""Flask web application for emotion detection."""

from flask import Flask, jsonify, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions from the supplied text."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!."

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    