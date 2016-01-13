my_energy_forecast_SVR
=========
This Github directory contains predicitive modeling of hourly electricity data for an apartment in Baltimore, MD.  The data are collected via smart meter installed by Baltimore Gas and Electric and obtained using the Green Button protocol (.csv output) from the BGE website.  A support vector regression is performed to predict hourly kilowatt-hour use in the apartment for the last week of March 2014.  

More details and description can be found on my website [The Training Set](http://www.thetrainingset.com).

# Data

data/elec_hourly_oldApt_2014-04-30.csv -- My hourly electricity use in kilowatt-hours exported from BGE website.  The model in [hourly_forecast_SVR.ipynb](hourly_forecast_SVR.ipynb) and [hourly_forecast_SVR_crossval_eval.ipynb](hourly_forecast_SVR_crossval_eval.ipynb) both use this dataset.

data/elec_hourly_newApt_2015-10-31.csv -- This is a download of the same dataset from my newer apartment, however I have not modeled electricity use for this apartment yet.

data/weather_2015-02-01.csv -- Hourly averages of weather variables obtained from Weather Underground via API.

# iPython Notebooks

hourly_forecast_SVR.ipynb -- Training a support vector machine to predict next-hour electricity consumption.

hourly_forecast_SVR_crossval_eval.ipynb -- Cross-validation for support vector model for prediction of next-hour electricity consumption.

# Python Codes and Scripts

history.py -- Creates additional fields that are equal to another field's values at specified lag times.  For instance, the electricity consumption at t-2 hours.

errors.py -- Functions that calculate various error measures for a model when given two Pandas dataframes, one containing the predicted values and the other containing the actual values.
  