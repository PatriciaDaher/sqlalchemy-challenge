# SQLAlchemy Challenge: Climate Analysis and Flask API

## Overview
This project involves analyzing climate data for Honolulu, Hawaii, using SQLAlchemy, Pandas, and Matplotlib. The analysis is based on a SQLite database containing weather station and measurement data. The project includes data exploration, visualization, and the creation of a Flask API to present the analyzed data.

## Project Structure
The repository is organized as follows:\
```
sqlalchemy-challenge
└── SurfsUp
    ├── Resources                  # Folder containing the SQLite database\
    │   ├── hawaii.sqlite
    │   ├── hawaii_measurements.csv
    │   └── hawaii_stations.csv
    ├── climate_starter.ipynb      # Jupyter Notebook for climate analysis\
    ├── app.py                     # Flask API script\
    └── README.md                  # Project documentation\
```
## Data Exploration and Analysis
The project involves two main parts: climate data analysis and the creation of a Flask API.

### Part 1: Climate Data Analysis

#### Precipitation Analysis:
1. Identified the most recent date in the dataset.
2. Retrieved the last 12 months of precipitation data.
3. Loaded the data into a Pandas DataFrame and plotted the results.
4. Calculated summary statistics for the precipitation data.

#### Station Analysis:
1. Calculated the total number of stations in the dataset.
2. Identified the most active station.
3. Retrieved the last 12 months of temperature observation data (TOBS) for the most active station.
4. Plotted the TOBS data as a histogram.

### Part 2: Flask API
The Flask API provides the following routes:
1. `/`: Homepage listing all available routes.
2. `/api/v1.0/precipitation`: Returns JSON of precipitation data for the last 12 months.
3. `/api/v1.0/stations`: Returns JSON of all stations in the dataset.
4. `/api/v1.0/tobs`: Returns JSON of temperature observations for the most active station for the previous year.
5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Returns JSON of min, max, and average temperatures for a specified date range when `<start>` and `<end>` are replaced by available dates in the format `MMDDYYYY`.

## Technologies Used
1. Python
2. SQLAlchemy
3. Pandas
4. Matplotlib
5. Flask

## Results
1. Precipitation Analysis
2. Station Analysis
3. Flask API

## License
Open Source
