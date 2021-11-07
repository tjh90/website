from flask import Flask
from flask import redirect
from flask import request

from src.FileContentProvider import FileContentProvider
from src.MobileContentProvider import MobileContentProvider
from src.Utils import isMobile

# Create server.
app = Flask(__name__)

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
