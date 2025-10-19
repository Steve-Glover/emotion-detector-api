from flask import Flask, render_template, resonse
from EmotionDetection import emotion_dector
import json


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = response.get.args("textToAnalyze")
    detected_emotion = json.load(emotion_dector(textToAnalyze))
    return_string = f"For the given statement, the system reponse is {detected_emotion}"
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
