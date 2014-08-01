""" Downloads weather data from weather underground API, loads into a pandas
dataframe, and saves to a .csv. Note that in the .csv, the index column is
unlabeled. This takes care of itself if you open it as a pandas dataframe, 
but is potentially confusing if used in another way.

Takes command line inputs of the month, day, and year of the start date and 
end date. For example, to download data for all of February, 2012, run:

python weather_download_observations.py 2 1 2012 2 29 2012

'use_save_to_path' is a boolean. If True, the .cvs will be save in the path
    specified by 'save_to_path'. If False, it is saved in the current directory.
'save_to_path' specificies where the .csv will be saved.
'key' is my API key from weather underground. My free account is limited to
    500 calls per day and 10 calls per minute.
'location' can be set to the ICAO id for an airport weather station
'empty_obs_dict' is a dictionary containing the observations to be downloaded. 
    A list of observations can be found at 
    http://www.wunderground.com/weather/api/d/docs?d=resources/phrase-glossary
    Note not all of those observations are available for historical data.

Some possible observations to download:
    tempm: Temperature in C
    hum: Humidity %
    wspdm: Wind speed in kph
    wgustm: Wind gust in kph
    wdird: Wind direction in degrees
    pressurem: Pressure in mBar
    precipm: Precipitation in mm
    conds: Conditions - this is words, like 'Overcast' or 'Light Drizzle'

-MYH 2/24/13

"""

import urllib2
import json
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import sys
import copy
import os

key = '9a059f2253d818e9' # my weather undergrount API key
location = 'KBWI' # the ICAO id for the Central Park weather station
empty_obs_dict = {'tempm':[], 'hum':[], 'wspdm':[], 'precipm':[], 'conds':[]}
save_to_path = '/Users/Justin/Dropbox/Analysis_and_Blog/'
use_save_to_path = False

def downloadOneDayObs(weather_date):
    YYYYMMDD = weather_date.strftime("%Y%m%d")
    query = ('http://api.wunderground.com/api/%s/history_%s/q/%s.json' 
            %(key, YYYYMMDD, location))
    f = urllib2.urlopen(query)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    prettydate = parsed_json['history']['date']['pretty']
    print prettydate
    return parsed_json

def getOneDayObs(parsed_json, input_dict):
    timestamp_list = []
    float_obs_dict = copy.deepcopy(input_dict)
    del float_obs_dict['conds']
    conds_list = []

    num_obs = len(parsed_json['history']['observations'])
    for i in range(num_obs):

        year = int(parsed_json['history']['observations'][i]['date']['year'])
        month = int(parsed_json['history']['observations'][i]['date']['mon'])
        day = int(parsed_json['history']['observations'][i]['date']['mday'])
        hour = int(parsed_json['history']['observations'][i]['date']['hour'])
        minute = int(parsed_json['history']['observations'][i]['date']['min'])
        timestamp_list.append(datetime(year, month, day, hour, minute))

        for obs in float_obs_dict:

            value = float(parsed_json['history']['observations'][i][obs])

            if value == -9999:
                value = np.nan
            float_obs_dict[obs].append(value)

        conds_list.append(parsed_json['history']['observations'][i]['conds'])

    obs_dict = float_obs_dict
    obs_dict['conds'] = conds_list

    return timestamp_list, obs_dict

def main():
    startMonth = int(sys.argv[1])
    startDay = int(sys.argv[2])
    startYear = int(sys.argv[3])
    endMonth = int(sys.argv[4])
    endDay = int(sys.argv[5])
    endYear = int(sys.argv[6])
    
    startDate = datetime(year=startYear, month=startMonth, day=startDay)
    endDate = datetime(year=endYear, month=endMonth, day=endDay)

    currentDate = startDate
    if currentDate > endDate:
        raise Exception, ('End date is before start date.\n Arguments should be:'
                ' startMonth startDay startYear endMonth endDay endYear')

    full_timestamp_list = []
    full_obs_dict = copy.deepcopy(empty_obs_dict)

    while currentDate <= endDate:
        parsed_json = downloadOneDayObs(currentDate)
        day_timestamp_list, day_obs_dict = getOneDayObs(parsed_json, empty_obs_dict)
        full_timestamp_list.extend(day_timestamp_list)
        {full_obs_dict[obs].extend(day_obs_dict[obs]) for obs in full_obs_dict}
        currentDate += timedelta(days=1)

    df = pd.DataFrame(full_obs_dict, index = full_timestamp_list)
    start_string = startDate.strftime("%Y%m%d")
    end_string = endDate.strftime("%Y%m%d")
    current = os.getcwd()
    if use_save_to_path == True:
        os.chdir(save_to_path)
    df.to_csv('weather_'+start_string+'to'+end_string+'_df.csv')
    os.chdir(current)
    print df

if __name__ == '__main__':
    main()