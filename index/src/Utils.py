import json
import os

from .FileContentProvider import FileContentProvider
from .MobileContentProvider import MobileContentProvider
from .eightball.EightBall import EightBall
from .eightball.Prediction import Prediction

def isMobile(request):
    '''
    Determine if the request was sent by a mobile agent.

    @param request the request.

    @returns True iff the user agent appears to be from a mobile device.
    '''

    agent = request.user_agent.string.lower()
    for keyword in ['android', 'iphone', 'mobile']:
        if keyword in agent:
            return True

    return False

def getStaticPage(request, filename):
    '''
    Get static content for an HTML page.

    @param request the request.
    @param filename the name of the HTML file to serve.

    @returns the HTML content.
    '''

    contentProvider = FileContentProvider(filename)

    if isMobile(request):
        contentProvider = MobileContentProvider(contentProvider)

    return contentProvider.getContent()

def eightBallFromFile(filename):
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

    eightBall = EightBall(predictions)

    return eightBall
