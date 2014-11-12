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
	weather = pd.read_csv('raw_data/weather/weather_2014-01.csv',skiprows=0)
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-02.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-03.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-04.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-05.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-06.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-07.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-08.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-09.csv',skiprows=0))
	weather = weather.append(pd.read_csv('raw_data/weather/weather_2014-10.csv',skiprows=0))

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

def BGEdata(loc):

	if loc == "old apt":
	# Add additional electricity usage csv's downloaded using Green Button protocol on BGE.com
		elec = pd.read_csv('raw_data/old_apt/elec_hourly_2014-01.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp')
		elec = elec.append(pd.read_csv('raw_data/old_apt/elec_hourly_2014-02.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/old_apt/elec_hourly_2014-03.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/old_apt/elec_hourly_2014-04.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))

	if loc == "new apt":
		elec = pd.read_csv('raw_data/new_apt/elec_hourly_2014-05-24_2014-05-31.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp')
		elec = elec.append(pd.read_csv('raw_data/new_apt/elec_hourly_2014-06.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/new_apt/elec_hourly_2014-07.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/new_apt/elec_hourly_2014-08.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/new_apt/elec_hourly_2014-09.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))
		elec = elec.append(pd.read_csv('raw_data/new_apt/elec_hourly_2014-10.csv',skiprows=0,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))

	return elec


