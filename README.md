# Wine Review API

This is a Flask-based API for retrieving data from a Wine database. The API supports basic authentication and provides endpoints to list, retrieve, add, and delete wine records.

## Features

- List all wines (currently disabled)
- Retrieve a specific wine by title
- Add a new wine to the database (currently disabled)
- Remove a wine from the database (currently disabled)
- Basic HTTP authentication

## Requirements

- Python 3.x
- Flask
- Flask-RESTx
- Flask-HTTPAuth
- SQLite3
- Werkzeug

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install Flask Flask-RESTx Flask-HTTPAuth
    ```

3. Set up environment variables for API authentication:
    ```sh
    export API_USERNAME=<your_username>
    export API_PASSWORD=<your_password>
    ```

4. Ensure you have a SQLite database named `wine_data.db` with a table `wines` containing the appropriate columns.

## Running the Application

Start the Flask application:
```sh
python app.py
```

The application will be available at http://0.0.0.0:5001.

## API Endpoints
### List All Wines
#### GET /wine/
- Description: List all wines (currently disabled).
- Authentication: Required

#### Retrieve a Specific Wine
#### GET /wine/<string:title>
- Description: Retrieve a specific wine by title.
- Authentication: Required

### Add a New Wine
#### POST /wine/<string:title>
- Description: Add a new wine to the database (currently disabled).
- Authentication: Required

### Remove a Wine
#### DELETE /wine/<string:title>
- Description: Remove a wine from the database (currently disabled).
- Authentication: Required

### Logging
The application logs messages to app.log with a maximum size of 1MB and keeps up to 5 backup files.

## Wine Data
The wine data used in this project is sourced from the following Kaggle dataset:

https://www.kaggle.com/datasets/zynicide/wine-reviews

The original data was scraped from the Wine Enthusiast website:
https://www.wineenthusiast.com

The database contains approximately 130,000 wine reviews.





