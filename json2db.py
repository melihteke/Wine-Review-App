import json
import sqlite3

# Path to the JSON file

json_file_path = 'winemag-data-130k-v2.json'

# Load JSON data from the file

with open(json_file_path, 'r') as json_file:
    wine_data = json.load(json_file)
    json_file.close()

# Path to the SQLite database

sqlite_db_path = 'wine_data.db'

# Connect to the SQLite database (or create it if it doesn't exist)

conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()

# Define the table schema

cursor.execute('''
CREATE TABLE IF NOT EXISTS wines (
id INTEGER PRIMARY KEY AUTOINCREMENT,
points TEXT,
title TEXT,
description TEXT,
taster_name TEXT,
taster_twitter_handle TEXT,
price REAL,
designation TEXT,
variety TEXT,
region_1 TEXT,
region_2 TEXT,
province TEXT,
country TEXT,
winery TEXT
)
''')

# Insert data into the SQLite database

for wine in wine_data:
    cursor.execute('''
    INSERT INTO wines (points, title, description, taster_name, taster_twitter_handle, price, designation, variety, region_1, region_2, province, country, winery)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    wine.get('points'),
    wine.get('title'),
    wine.get('description'),
    wine.get('taster_name'),
    wine.get('taster_twitter_handle'),
    wine.get('price'),  # Assuming price is None if not available
    wine.get('designation'),
    wine.get('variety'),
    wine.get('region_1'),
    wine.get('region_2'),
    wine.get('province'),
    wine.get('country'),
    wine.get('winery')
    ))

# Commit the transaction

conn.commit()

# Close the connection

conn.close()

print(f"Data from {json_file_path} has been inserted into {sqlite_db_path}")