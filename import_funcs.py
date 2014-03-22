import sys
import numpy as np
import pandas as pd
from datetime import datetime
import time_parser
#reload(time_parser)

def weather():

	weather = pd.read_csv('weather_20140101to20140131_df.csv',skiprows=0)
	weather = weather.append(pd.read_csv('weather_20140201to20140228_df.csv',skiprows=0))

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

	DF = pd.read_csv('raw_data/DailyElectricUsage_201401.csv',skiprows=4,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp')
	DF = DF.append(pd.read_csv('raw_data/DailyElectricUsage_201402.csv',skiprows=4,parse_dates={'timestamp':['DATE','START TIME'],'timestamp_end':['DATE','END TIME']},index_col='timestamp'))


	return DF


