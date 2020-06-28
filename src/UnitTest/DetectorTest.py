import unittest
from src.DiseaseDetector import DiseaseDetector
import cv2
import os


class MyTestCase(unittest.TestCase):
    def test_detector(self):
        detector = DiseaseDetector()
        cur_path = os.getcwd()

        right_img = cv2.imread(cur_path + "/1224.png")
        right_img = cv2.cvtColor(right_img, cv2.COLOR_BGR2RGB)

        big_img = cv2.imread(cur_path + "/healthy.png")
        big_img = cv2.cvtColor(big_img, cv2.COLOR_BGR2RGB)

        response_one = detector.detect(right_img)
        response_two = detector.detect(big_img)

        self.assertTrue(response_one)
        self.assertFalse(response_two)


if __name__ == '__main__':
    unittest.main()
