# <!-- ### Part 2: Design Your Climate App

from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import distinct

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

# Import API key
from api_keys import password

# Import Python File
import scrape_mars

# Initialize PyMongo to work with MongoDBs
# client = pymongo.MongoClient("mongodb+srv://admin:" + password + "@cluster0.0dopl0q.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

# Define database and collection
db = client.test
collection = db.items

app = Flask(__name__)
from flask_pymongo import PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# * `/`
#     * Homepage.
#     * Create a root route / that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars=mars)

# * `/api/v1.0/scrape`
#     * Call scrape function. Store the return value in Mongo as a Python dictionary.
#     * Return the JSON representation of your dictionary.

@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_info()

    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)

    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)