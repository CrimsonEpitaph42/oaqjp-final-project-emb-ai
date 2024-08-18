'''Module for detecting emotion in text using the Watson NLP library'''

import requests
import json

WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
WATSON_PREDICTION_KEY = 'emotionPredictions'
EMOTIONS_KEY = 'emotion'

def emotion_detector(text_to_analyze):
    text_json = {"raw_document": {"text" : text_to_analyze}}
    res = requests.post(url=WATSON_URL, json=text_json, headers=WATSON_HEADERS)
    res_json = json.loads(res.text)
    res_emotions = res_json[WATSON_PREDICTION_KEY][0][EMOTIONS_KEY]

    dominant_emotion = ""
    max_score = 0
    for emotion in res_emotions.keys():
        if res_emotions[emotion] > max_score:
            max_score = res_emotions[emotion]
            dominant_emotion = emotion

    ret = {
        'anger': res_emotions['anger'],
        'disgust': res_emotions['disgust'],
        'fear': res_emotions['fear'],
        'joy': res_emotions['joy'],
        'sadness': res_emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return ret
    
if __name__ == "__main__":
    print(emotion_detector("I love this tech"))
