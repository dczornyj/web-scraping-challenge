from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"]= 'mongodb://localhost:27017/mars_app'
mongo=PyMongo(app)

@app.route("/")
def home():    
    # Find one record of data from the mongo database
    mars_page_scraped = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_page_scraped, )


@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_data()

    #for loop for images in mars hemisphere
    
    # Insert the record
    mongo.db.collection.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
