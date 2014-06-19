my_energy
=========
This Github directory contains analysis and predicitive modeling of hourly electricity data for an apartment in Baltimore, MD.  The data are collected via smart meter installed by Baltimore Gas and Electric and obtained using the Green Button protocol (.csv output) from the BGE website.

## iPython Notebooks

  My_Energy.ipynb -- Exploratory data analysis for hourly electricity usage at an apartment in Baltimore, Maryland.

  My_Energy_and_Weather.ipynb -- Exploring the correlation between outdoor weather and electricity consumption.

  Usage_Autocorrelation.ipynb -- Checking for autocorrelation in electricity consumption.

  forecasts/Elec_SVM.ipynb -- Training a support vector machine to predict next-hour electricity consumption.

  forecasts/Elec_SVM_crossval.ipynb -- Cross-validation for support vector model for prediction of next-hour electricity consumption.

## Python Codes and Scripts

  time_parser.py -- Needed to interpret the timestamps from NOAA's weather files.
  
  import_funcs.py -- A couple of functions to smash a bunch of csv files into Pandas dataframes.  Currently includes functions for the BGE electricity data and for the NOAA weather data.
  
  history.py -- Creates additional fields that are equal to another field's values at specified lag times.  For instance, the electricity consumption at t-2 hours.
  
  errors.py -- Functions that calculate various error measures for a model when given two Pandas dataframes, one containing the predicted values and the other containing the actual values.
  
  weather_download_observations.py --  Downloads weather data for a specified timeframe from wunderground.com.  Originally written by Melinda Han at Columbia University.

## Plots

  plots/

## Datasets

  BGE

  NOAA weather