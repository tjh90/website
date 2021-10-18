from flask import Flask
from flask import redirect
from flask import request

# Create server.
app = Flask(__name__)

@app.before_request
def redirectHttp():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# Routes.
@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()
