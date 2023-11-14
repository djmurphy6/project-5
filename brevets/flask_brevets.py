"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask, os, pymongo
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
from pymongo import MongoClient

import logging

# create mongo client
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html', 
                    items=list(db.controls.find()))


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 0, type=float)
    app.logger.debug("km={}".format(km))

    # get starting time
    time = request.args.get('time', type = str)
    app.logger.debug("time={}".format(time))

    # get brevet distance
    dist = flask.request.args.get("dist", type=int)
    app.logger.debug("dist={}".format(dist))

    # if checkpoint is further than distance, set km to distance
    # if km > dist:
    #    km = dist

    app.logger.debug("request.args: {}".format(request.args))
    


    open_time = acp_times.open_time(km, dist, time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, dist, time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/submit", methods=["POST"])
def submit():
    # Get the JSON data from the request
    data = request.get_json()
    

    # Extract data from the JSON data
    brevet_distance = data.get('brevetDistance')
    # app.logger.debug("brevet_distance={}".format(brevet_distance))
    begin_date = data.get('beginDate')
    # app.logger.debug("begin_date={}".format(begin_date))
    controls = data.get('tableData', [])
    # app.logger.debug("controls={}".format(controls))

    # Create a MongoDB document
    document = {
        "brevet_distance": brevet_distance,
        "begin_date": begin_date,
        "controls": controls
    }

    # Insert the document into the MongoDB collection
    db.controls.insert_one(document)

    return "Data submitted successfully"

@app.route("/display")
def display():
    # Fetch most recent document from the MongoDB collection
    mr_doc = db.controls.find_one(sort=[('_id', pymongo.DESCENDING)])

    # Convert ObjectId to string
    mr_doc['_id'] = str(mr_doc['_id'])
    
    # Log the fetched data
    app.logger.debug("Data: {}".format(mr_doc))

    # Return the data as JSON
    return flask.jsonify(result=mr_doc)

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
