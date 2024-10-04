from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Hello, World! <a href="/about">About</a></p>'

@app.route('/about')
def about():
    return '<p>This is a Flask web app running in a Linux VM.</p>'
