'''Module for detecting emotion in text using the Watson NLP library'''

import requests
import json

WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
WATSON_PREDICTION_KEY = 'emotionPredictions'
EMOTIONS_KEY = 'emotion'

def emotion_detector(text_to_analyze):
    text_json = {"raw_document": {"text" : text_to_analyze}}

    anger_res = None
    disgust_res = None
    fear_res = None
    joy_res = None
    sadness_res = None
    dominant_emotion = None

    res = requests.post(url=WATSON_URL, json=text_json, headers=WATSON_HEADERS)
    if res.status_code != 400:
        res_json = json.loads(res.text)
        res_emotions = res_json[WATSON_PREDICTION_KEY][0][EMOTIONS_KEY]

        max_score = 0
        for emotion in res_emotions.keys():
            if res_emotions[emotion] > max_score:
                max_score = res_emotions[emotion]
                dominant_emotion = emotion

            anger_res = res_emotions['anger']
            disgust_res = res_emotions['disgust']
            fear_res = res_emotions['fear']
            joy_res = res_emotions['joy']
            sadness_res = res_emotions['sadness']

    # If the status code is 400, these will all be None
    ret = {
        'anger': anger_res,
        'disgust': disgust_res,
        'fear': fear_res,
        'joy': joy_res,
        'sadness': sadness_res,
        'dominant_emotion': dominant_emotion
    }
    return ret
    
if __name__ == "__main__":
    print(emotion_detector("I love this tech"))
