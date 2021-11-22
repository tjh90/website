class Prediction:
    ''' Class to encapsulate a prediction. '''

    def __init__(self, id, severity, msg):
        '''
        Constructor.

        @param id the prediction ID.
        @param severity the prediction severity.
        @param msg the prediction message.
        '''

        self.__id = id
        self.__severity = severity
        self.__msg = msg

    def getId(self):
        return self.__id

    def getSeverity(self):
        return self.__severity

    def getMsg(self):
        return self.__msg
