from flask import Flask, render_template, request, make_response
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
    if detected_emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again", 200

    return f"For the given statement, the system reponse is {detected_emotion}"

 
if __name__ == "__main__":
    app.run(port=5000, debug=True)
