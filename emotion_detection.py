'''Module for detecting emotion in text using the Watson NLP library'''

import requests

WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    text_json = {"raw_document": {"text" : text_to_analyze}}
    res = requests.post(url=WATSON_URL, json=text_json, headers=WATSON_HEADERS)
    return res.text