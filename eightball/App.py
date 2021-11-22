from flask import jsonify, Flask, redirect, request

from predict.EightBall import EightBall

# Create server.
app = Flask(__name__, static_folder='./build/static')

# Create eight ball instance.
eightBallInst = EightBall.fromFile('predictions.json')

# Routes.
@app.route('/')
def root():
    ''' Redirect to index page. '''

    url = request.url + 'index.html'
    return redirect(url, code=301)

@app.route('/index.html')
def index():
    ''' Return index page. '''

    with open('./build/index.html', 'r') as file:
        return file.read()

@app.route('/predict')
def eightBallPredict():
    ''' Get an 8 ball prediction. '''

    response = jsonify(eightBallInst.predict())
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
