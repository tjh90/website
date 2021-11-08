import random

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
