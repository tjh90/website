from flask import Flask

# Create server.
app = Flask(__name__)

# Routes.
@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()
