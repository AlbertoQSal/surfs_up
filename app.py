from flask import Flask

app = Flask(__name__)
@app.route('/') # Set the root


def hello_world():
    return 'Hello world'
