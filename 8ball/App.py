from flask import Flask, redirect, request

# Create server.
app = Flask(__name__, static_folder='./build/static')

# Routes.
@app.route('/')
def root():
    ''' Return index page. '''

    with open('./build/index.html', 'r') as file:
        return file.read()
