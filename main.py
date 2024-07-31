from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

API_USERNAME = os.environ['API_USERNAME']
API_PASSWORD = os.environ['API_PASSWORD']

# In-memory user storage for demonstration
users = {
    f'{API_USERNAME}' : generate_password_hash(API_PASSWORD)
}

# Basic authentication callback
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# Define a namespace for the API
ns = api.namespace('wine', description='Wine DB operations')

@ns.route('/')
class WineList(Resource):
    @auth.login_required
    def get(self):
        """List all wines"""

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

        return result_list

    @auth.login_required
    def post(self, title):
        """Add a new wine to DB"""
        return jsonify({"operation": f"{title} is added",
                        "message": "this endpoint is disabled on purpose. Nothing is changed on database."})
    
    @auth.login_required
    def delete(self, title):
        """Remove a wine from DB"""
        return jsonify({"operation": f"{title} is removed",
                        "message": "this endpoint is disabled on purpose. Nothing is changed on database."})
    
# Run the Flask application
if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5001)