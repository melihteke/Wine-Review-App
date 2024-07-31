from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import sqlite3
import os
import logging
from logging.handlers import RotatingFileHandler



# Initialize Flask app
app = Flask(__name__)
api = Api(app, description="Wine Review API", version='1.0.1')

# logging configuration
log_file = "app.log"
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"
# Create a rotating file handler that logs messages to a file with a maximum size of 1MB,
# and keeps up to 5 backup files.
handler = RotatingFileHandler(log_file, maxBytes=1*1024*1024, backupCount=5)
handler.setFormatter(logging.Formatter(fmt=log_format, datefmt=date_format))

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the logging level to the lowest level
logger.addHandler(handler)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()


API_USERNAME = os.environ['API_USERNAME']
API_PASSWORD = os.environ['API_PASSWORD']
logger.debug("Environment variables are loaded")

# In-memory user storage for demonstration
users = {
    f'{API_USERNAME}' : generate_password_hash(API_PASSWORD)
}

# Basic authentication callback
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        logger.debug("Verify password operation is done.")
        return username

# Define a namespace for the API
ns = api.namespace('wine', description='Wine DB operations')

@ns.route('/')
class WineList(Resource):
    @auth.login_required
    def get(self):
        """List all wines"""
        logger.info("Retrived all wine list.")
        return jsonify({"operation": "Retrieve all the wines list.",
                        "message": "this endpoint is disabled on purpose."})
    

@ns.route('/<string:title>')
class Wine(Resource):
    @auth.login_required
    def get(self, title):
        """Get a specific wine by title"""
        # Here, you would normally fetch the wine details
        sqlite_db_path = "wine_data.db"

        conn = sqlite3.connect(sqlite_db_path)

        cursor = conn.cursor()

        search_term = title

        cursor.execute('SELECT points, title, description, taster_name, taster_twitter_handle,  price, designation, variety, region_1, region_2, province, country, winery FROM wines WHERE title LIKE ?', ('%' + search_term + '%',))
        results = cursor.fetchall()

        result_list = []
        for point, title, description, tester_name, taster_twitter_handle, price, designation, variety, region_1, region_2, province, country, winery in results:
            result_list.append({"points": point,
                                "title": title,
                                "description": description,
                                "taster_name": tester_name,
                                "taster_twitter_handle": taster_twitter_handle,
                                "price": price,
                                "designation": designation,
                                "variety": variety,
                                "region_1": region_1,
                                "region_2": region_2,
                                "province": province,
                                "country" : country,
                                "winery" : winery,
                                })
        logger.info(f"Retrived single wine: '{title}' data.")
        return result_list

    @auth.login_required
    def post(self, title):
        """Add a new wine to DB"""
        logger.info(f"Added single wine: '{title}' data.")
        return jsonify({"operation": f"{title} is added",
                        "message": "this endpoint is disabled on purpose. Nothing is changed on database."})
    
    @auth.login_required
    def delete(self, title):
        """Remove a wine from DB"""
        logger.info(f"Deleted single wine: '{title}' data.")
        return jsonify({"operation": f"{title} is removed",
                        "message": "this endpoint is disabled on purpose. Nothing is changed on database."})
    
# Run the Flask application
if __name__ == '__main__':
     logger.info("Application is started.")
     app.run(debug=True, host='0.0.0.0', port=5001)