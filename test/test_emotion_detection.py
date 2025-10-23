import unittest
from unittest import TestCase
from nlp import emotion_detector

class TestNLPEmotionDetection(TestCase):

    def test_dominant_emotion(self):
        tests = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        for text, expected in tests:
            with self.subTest(text=text, expected=expected):
                result = emotion_detector(text)['dominant_emotion']
                self.assertEqual(result, expected)


if __name__== '__main__':
    unittest.main(verbosity=2)