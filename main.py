from flask import Flask
import os
from flask import Flask, render_template
from flask_restx import Api, Resource, reqparse

# Initialize Flask app and Api
app = Flask(__name__)
api = Api(app, title='Heroku API', version='1.0', description='API collection for www.mteke.com applications')

# Define a Retail Voice namespace
ns1 = api.namespace('', description='mteke.com APIs')

@ns1.route('/')
class HelloWorld(Resource):
    def get(self):
        NAME = os.environ['NAME']
        SURNAME = os.environ['SURNAME']
        return f'Hello, {NAME} {SURNAME}!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
