"""
import_funcs.py class has two functions - weather() and BGEdata()


weather() aggregates and returns a Pandas dataframe with hourly weather readings. The csv files
are hourly weather observations from weatherunderground.com using 'weather_download_observations.py'
Add additional csv's using weather.append.
params: none
returns: 'weather' - Pandas dataframe, hourly weather data

BGEdata() aggregates and returns a Pandas dataframe with hourly electricity usage from BGE.com.
params: none
returns: 'DF' - Pandas dataframe, hourly electricity usage


Justin Elszasz 2014.04.10
"""

import sys
import numpy as np
import pandas as pd
from datetime import datetime
import time_parser

def weather():

	# Add additional weather csv's downloaded using 'weather_download_obeservations.py' here
	weather = pd.read_csv('raw_data/weather_20140101to20140131_df.csv',skiprows=0)
	weather = weather.append(pd.read_csv('raw_data/weather_20140201to20140228_df.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather_20140301to20140331_df.csv',skiprows=0))

	weather['timestamp'] = weather.iloc[:,0]
	weather.index = pd.to_datetime(weather['timestamp'])
	
	#bcWeather.index = list(xrange(len(bcWeather['YR--MODAHRMN'])))

	# Adding hour offset because resampling floors the hour, but all are past 50 min mark
	weather = weather.resample('h',fill_method='ffill',loffset='1h')
	
	#cWeather['timestamp'] = time_parser.time_parser(bcWeather['Date'],bcWeather['Time'])
	#bcWeather.index = bcWeather['timestamp']
	
	weather['tempF'] = weather['tempm']*9./5. + 32.
	weather['tempF'] = weather['tempF'].apply(lambda x: round(x,1))

	return weather

def BGEdata():

	# Add additional electricity usage csv's downloaded using Green Button protocol on BGE.com
	elec = pd.read_csv('raw_data/DailyElectricUsage_201401.csv',skiprows=4,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp')
	elec = elec.append(pd.read_csv('raw_data/DailyElectricUsage_201402.csv',skiprows=4,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
	elec = elec.append(pd.read_csv('raw_data/DailyElectricUsage_201403.csv',skiprows=5,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))

	return elec


