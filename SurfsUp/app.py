# Import the dependencies.

import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model(# Create engine using the `hawaii.sqlite` database file 
#engine = create_engine("sqlite:///Resources/hawaii.sqlite")
engine = create_engine("sqlite:////Users/patriciadaher/Desktop/ColumbiaDA/Homework/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")

# Declare a Base using `automap_base()
Base = automap_base()

# reflect the tables ( Use the Base class to reflect the database tables )
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement  # Reference to the 'measurement' table
Station = Base.classes.station  

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# create an app, being sure to pass the name?
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define what to do when someone hits the index route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the most recent date in the dataset
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
   
    # Closing session
    session.close()

    # Create a dictionary from the query results
    precip = {date: prcp for date, prcp in precipitation_data}
    
    # Return the JSON representation of the dictionary
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Return a list of stations
    results = session.query(Station.station).all()

    # Closing session
    session.close()

    # Convert the list of tuples into a flat list
    stations = [result[0] for result in results]

    # Return the list as a JSON response
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Calculate the date one year ago from the most recent date in the dataset
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the last 12 months of temperature observation data for this station
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    #closing session
    session.close()

    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # Define the selection query for min, avg, and max temperatures
    sel = [
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ]

    # Parse the start date
    start = dt.datetime.strptime(start,'%m%d%Y')

    if not end:
        # Query for dates greater than or equal to the start date
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
    else:
        # Parse the end date
        end = dt.datetime.strptime(end,'%m%d%Y')

        # Query for dates between the start and end dates
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

    # Close the session
    session.close()

    # Convert the results into a list of dictionaries for better readability
    temps = [{"Min Temperature": result[0],
              "Avg Temperature": result[1],
              "Max Temperature": result[2]} for result in results]

    # Return the results as a JSON response
    return jsonify(temps)


if __name__=="__main__":
    app.run(debug=True)



# RESULTS 
# details about precipitations
# stations 
# statistics max mean average 

