from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    detected_emotion = emotion_detector(textToAnalyze)
    return f"For the given statement, the system reponse is {detected_emotion}"

    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
