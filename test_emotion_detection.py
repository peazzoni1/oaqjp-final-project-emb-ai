import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_successful_emotion_detection_joy(self):
        # Call the function
        result = emotion_detector("I am glad this happened")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_successful_emotion_detection_anger(self):
        # Call the function
        result = emotion_detector("I am really mad about this")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_successful_emotion_detection_digust(self):
        # Call the function
        result = emotion_detector("I feel disgusted just hearing about this")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_successful_emotion_detection_sadness(self):
        # Call the function
        result = emotion_detector("I am so sad about this")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_successful_emotion_detection_fear(self):
        # Call the function
        result = emotion_detector("I am really afraid that this will happen")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()