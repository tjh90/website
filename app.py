from flask import Flask, jsonify, redirect, request

from src.Utils import eightBallFromFile, getStaticPage

# Create server.
app = Flask(__name__)

# Create 8ball instance.
eightBallInst = eightBallFromFile('./predictions.json')

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

    return getStaticPage(request, 'static/index.html')

@app.route('/8ball.html')
def eightBall():
    ''' Serve 8 ball page. '''

    return getStaticPage(request, 'static/8ball.html')

@app.route('/8ball/predict')
def eightBallPredict():
    ''' Get an 8 ball prediction. '''

    response = jsonify(eightBallInst.predict())
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
