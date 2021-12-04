from flask import abort, Flask, redirect, render_template, request, send_from_directory
import os

import src.Utils as Utils

# Create server.
app = Flask(__name__)

@app.before_request
def redirectHttp():
    ''' Redirect HTTP requests to HTTPS. '''

    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/robots.txt')
def robots():
    ''' Get robots.txt info. '''

    return send_from_directory(app.static_folder, 'robots.txt')

# Routes.
@app.route('/')
def root():
    ''' Redirect to index page. '''

    url = request.url + 'index.html'
    return redirect(url, code=301)

@app.route('/index.html')
def index():
    ''' Get index page. '''

    if Utils.isMobile(request):
        title = 'Tim\'s Mobile Page'
    else:
        title = 'Tim\'s Page'

    return render_template('index.html', title=title)

@app.route('/eightball.html')
def eightBall():
    ''' Serve 8 ball page. '''

    eightBallServerUrl = os.getenv('EIGHTBALL_SERVER_URL')
    if eightBallServerUrl is None:
        return abort(500)

    return render_template('eightball.html', eightBallServerUrl=eightBallServerUrl)
