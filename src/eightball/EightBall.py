import json
import os
import random

from .Prediction import Prediction

class EightBall:
    ''' Class to represent an 8-ball. '''

    def __init__(self, predictions):
        '''
        Constructor.

        @param predictions a list of possible predictions.
        '''

        self.__predictions = predictions

    def predict(self):
        '''
        Make a prediction.

        @returns JSON containing the prediction string.
        '''

        numPredictions = len(self.__predictions)
        probabilities = [1.0 / numPredictions for i in range(0,numPredictions)]
        prediction = random.choices(self.__predictions, weights=probabilities)[0]

        return {'msg':prediction.getMsg()}

    @staticmethod
    def fromFile(filename):
        '''
        Initialise a new EightBall from a config file.

        @param filename the name of the config file.
        '''

        if not filename.endswith('json'):
            raise RuntimeException('Config filename had unrecognised extension')
        elif not os.path.exists(filename) or not os.path.isfile(filename):
            raise FileNotFoundError('Config file does not exist')

        with open(filename, 'r') as file:
            content = file.read()
            rawJson = json.loads(content)

        id = 1
        predictions = []
        for prediction in json.loads(content):
            predictions.append(Prediction(id, prediction['severity'], prediction['msg']))

        return EightBall(predictions)
