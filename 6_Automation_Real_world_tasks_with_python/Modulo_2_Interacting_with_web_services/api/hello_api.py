# This is not an excutable code block
from flask import Flask

app = Flask("myapp")

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'