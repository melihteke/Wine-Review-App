import os
from flask import Flask, render_template, jsonify
from flask_restx import Api, Resource, reqparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_httpauth import HTTPTokenAuth

# Initialize Flask app and Api
app = Flask(__name__)
auth = HTTPTokenAuth("Bearer")
api = Api(app, title='Heroku API', version='1.0', description='API collection for www.mteke.com applications')

# Initialize the limiter
#limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"], storage_uri="memory://")

tokens= {
    "token1": "qwert",
    "token2": "12345"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    return None




# Define a Retail Voice namespace
ns1 = api.namespace('', description='mteke.com APIs')


@ns1.route('/public')
@auth.login_required
class Baerer(Resource):
    def get(self):
        return f'Hello, Bearer Token Authentication!', 200


@ns1.route('/hello')
#@limiter.limit("5 per minute")
class HelloWorld(Resource):
    def get(self):
        NAME = os.environ['NAME']
        SURNAME = os.environ['SURNAME']
        return f'Hello, {NAME} {SURNAME}!', 200

@ns1.route('/con')
#@limiter.limit("5 per minute")
class HelloWorld(Resource):
    def get(self):
        NAME = os.environ['NAME']
        SURNAME = os.environ['SURNAME']
        return f'{NAME} + {SURNAME}!', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
