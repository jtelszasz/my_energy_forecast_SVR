import sys
import numpy as np
import pandas as pd
from datetime import datetime

# this parser deals with the timestamps from the NOAA datasets with 2, 3, or 4 digits for minutes or hours+minutes
def time_parser(date_data,time_data):

	#initialize some columns
	minute = pd.DataFrame(np.zeros(len(time_data)))
	hour = pd.DataFrame(np.zeros(len(time_data)))
	second = pd.DataFrame(np.zeros(len(time_data)))
	timestamp = pd.DataFrame(np.zeros(len(time_data)))


	for i in range(len(time_data)):

		if len(str(time_data.loc[i])) == 2:
			minute.loc[i] = time_data.loc[i]

		if len(str(time_data.loc[i])) == 3:
			hour.loc[i] = str(time_data[i])[0]
			minute.loc[i] = str(time_data[i])[1:	]

		if len(str(time_data.loc[i])) == 4:
			temp = datetime.strptime(str(time_data.loc[i]),'%H%M')
			hour.loc[i] = temp.hour
			minute.loc[i] = temp.minute

	for j in range(len(time_data)):

		if minute.loc[j] >= 30:

			if hour.loc[j] == 23:
				hour.loc[j] = 0.0
			else:
				hour.loc[j] = hour.loc[j] + 1

		minute.loc[j] = 0.0
			


	years = date_data.apply(lambda x:x.year).apply(lambda x:np.int64(x))
	months = date_data.apply(lambda x:x.month).apply(lambda x:np.int64(x))
	days = date_data.apply(lambda x:x.day).apply(lambda x:np.int64(x))
	hour = hour.apply(lambda x:np.int64(x))
	minute = minute.apply(lambda x:np.int64(x))
	second = second.apply(lambda x:np.int64(x))

	timestamp = timestamp.apply(lambda x:pd.to_datetime(x))

	for k in range(len(timestamp)):
		timestamp.loc[k] = datetime(years.loc[k],months.loc[k],days.loc[k],hour.loc[k],minute.loc[k],second.loc[k])

	return timestamp




