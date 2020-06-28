from keras.models import load_model
import numpy as np
import pathlib
import os


class DiseaseDetector:
    model = None

    '''
        Instantiate this class ony once, as the constructor is slow
    '''
    def __init__(self):
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        path = str(pathlib.Path(__file__).parent.absolute())
        self.model = load_model(path + "/TreeColor.hdf5")

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    '''
        Image is supposed to be an OpenCV (CV2) image
        The color scheme must be RGB (OpenCV main scheme is BRG)
        Use cv2.cvtColor to convert color schemes
        
        Returns true if the plant is sick
    '''
    def detect(self, image):
        shape = image.shape

        if shape[0] < 128 or shape[1] < 128:
            return False

        if shape[0] > 128:
            middle_x = int(shape[0] / 2)
            middle_y = int(shape[1] / 2)

            xi = middle_x - 64
            xf = middle_x + 64

            yi = middle_y - 64
            yf = middle_y + 64

            image = image[xi:xf, yi:yf]

        image = np.array(image)
        image = image.astype(float)
        image = image / 255
        image = np.reshape(image, (1, 128, 128, 3))

        pred = self.model.predict(image)
        pred = np.reshape(pred, 1)
        pred = self.sigmoid(pred)

        if pred > 0.9:
            return True

        else:
            return False
