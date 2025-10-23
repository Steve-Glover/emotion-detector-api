""" Module API Documentation """
from flask import Flask, render_template, request
from nlp import emotion_detector


app = Flask(__name__)

@app.route("/")
def root():
    """root route"""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_api():
    """API emotion detector call"""
    text_to_analyze = request.args.get("textToAnalyze")
    detected_emotion = emotion_detector(text_to_analyze)
    if detected_emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again", 200

    return f"For the given statement, the system reponse is {detected_emotion}"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
