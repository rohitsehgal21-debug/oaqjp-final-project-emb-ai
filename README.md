# Emotion Detector

## Final Project – Emotion Detection Application

This project is an Emotion Detection application developed as part of the IBM/Coursera Final Project.

The application uses the Watson NLP Emotion Detection service to analyze a given text and identify the emotions expressed in the text.

## Project Objective

The objective of this project is to develop and deploy a web-based emotion detection application that:

- Accepts text entered by the user.
- Analyzes the text using the Watson NLP Emotion Detection service.
- Identifies five emotions:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Determines the dominant emotion.
- Provides the result through a Flask web application.
- Handles invalid or empty input appropriately.

## Project Structure

```text
EmotionDetectorRohit/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
