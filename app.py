from flask import Flask, jsonify, redirect, request

from src.eightball.EightBall import EightBall
from src.FileContentProvider import FileContentProvider
from src.MobileContentProvider import MobileContentProvider
from src.Utils import isMobile

# Create server.
app = Flask(__name__)

# Create 8ball instance.
eightBall = EightBall.fromFile('./predictions.json')

@app.before_request
def redirectHttp():
    ''' Redirect HTTP requests to HTTPS. '''

    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# Routes.
@app.route('/')
def root():
    ''' Redirect to index page. '''

    url = request.url + 'index.html'
    return redirect(url, code=301)

@app.route('/index.html')
def index():
    ''' Get index page. '''

    contentProvider = FileContentProvider('static/index.html')

    if isMobile(request):
        contentProvider = MobileContentProvider(contentProvider)

    return contentProvider.getContent()

@app.route('/8ball/predict')
def eightBallPredict():
    ''' Get an 8 ball prediction. '''

    response = jsonify(eightBall.predict())
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
