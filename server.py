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
    if textToAnalyze is None or textToAnalyze == "":
        response =  make_response("empty string supplied", 500) 
        return response
    detected_emotion = emotion_detector(textToAnalyze)
    return f"For the given statement, the system reponse is {detected_emotion}"

    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
