'''Test module for emotion_detection.py file'''

import unittest
import EmotionDetection.emotion_detection

JOY_STATEMENT = "I am glad this happened"
ANGER_STATEMENT = "I am really mad about this"
DISGUST_STATEMENT = "I feel disgusted just hearing about this"
SADNESS_STATEMENT = "I am so sad about this"
FEAR_STATEMENT = "I am really afraid that this will happen"

JOY_EMOTION = 'joy'
ANGER_EMOTION = 'anger'
DISGUST_EMOTION = 'disgust'
SADNESS_EMOTION = 'sadness'
FEAR_EMOTION = 'fear'
DOMINANT_EMOTION = "dominant_emotion"

CORRECT_RESPONSES = {
    JOY_STATEMENT: JOY_EMOTION,
    ANGER_STATEMENT: ANGER_EMOTION,
    DISGUST_STATEMENT: DISGUST_EMOTION,
    SADNESS_STATEMENT: SADNESS_EMOTION,
    FEAR_STATEMENT: FEAR_EMOTION
}

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        res = EmotionDetection.emotion_detection.emotion_detector(JOY_STATEMENT)
        self.assertEqual(res[DOMINANT_EMOTION], CORRECT_RESPONSES[JOY_STATEMENT])

    def test_anger(self):
        res = EmotionDetection.emotion_detection.emotion_detector(ANGER_STATEMENT)
        self.assertEqual(res[DOMINANT_EMOTION], CORRECT_RESPONSES[ANGER_STATEMENT])

    def test_disgust(self):
        res = EmotionDetection.emotion_detection.emotion_detector(DISGUST_STATEMENT)
        self.assertEqual(res[DOMINANT_EMOTION], CORRECT_RESPONSES[DISGUST_STATEMENT])

    def test_sadness(self):
        res = EmotionDetection.emotion_detection.emotion_detector(SADNESS_STATEMENT)
        self.assertEqual(res[DOMINANT_EMOTION], CORRECT_RESPONSES[SADNESS_STATEMENT])

    def test_fear(self):
        res = EmotionDetection.emotion_detection.emotion_detector(FEAR_STATEMENT)
        self.assertEqual(res[DOMINANT_EMOTION], CORRECT_RESPONSES[FEAR_STATEMENT])

if __name__ == "__main__":
    unittest.main()

