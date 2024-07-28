from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, {NAME} {SURNAME}!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
