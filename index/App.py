from flask import abort, Flask, redirect, render_template, request, send_from_directory
from markupsafe import Markup
import os

import src.Utils as Utils

# Create server.
app = Flask(__name__)

# Get environment variables.
appServerUrl = os.getenv('APP_SERVER_URL')

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
        imgContent = ''
    else:
        title = 'Tim\'s Page'
        imgContent = Markup('<img src="/static/sisley.jpg" alt="Sisley - Lady\'s Cove (1897)" />')

    return render_template('index.html', title=title, imgContent=imgContent)

@app.route('/eightball.html')
def eightBall():
    ''' Serve 8 ball page. '''

    if appServerUrl is None:
        return abort(500)

    return render_template('eightball.html', title='8-ball', appServerUrl=appServerUrl)

@app.route('/anascramble.html')
def anascramble():
    ''' Serve anascramble page. '''

    if appServerUrl is None:
        return abort(500)

    return render_template('anascramble.html', title='Anascramble', appServerUrl=appServerUrl)

@app.route('/music.html')
def music():
    ''' Serve music page. '''

    return render_template('music.html', title='Music')
