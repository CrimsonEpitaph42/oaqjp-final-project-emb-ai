'''Server file for the emotion detection app'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args["textToAnalyze"]
    results = emotion_detector(text_to_analyze)
    response_text = ""
    if results["dominant_emotion"]:
        response_text = f'For the given statement, the system response is \'anger\': {results["anger"]}, \'disgust\': {results["disgust"]}, \'fear\': {results["fear"]}, \'joy\': {results["joy"]} and \'sadness\': {results["sadness"]}.\n The dominant emotion is {results["dominant_emotion"]}'
    else:
        response_text = "Invalid text! Please try again!"
    return response_text, 200
    

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)