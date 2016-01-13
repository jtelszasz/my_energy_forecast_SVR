'''
history.py

Created by Justin Elszasz, 05.20.2014

Contains functions by which a Pandas dataframe can be appended with a variable's own history.
Useful if trying to predict future values based on past values.

history.append_history - appends each row with specified previous values for a given field
history.append_history_diff - appends each row with the differences between the specfied timesteps

df: Pandas dataframe
var: string of column name of interest
n_timesteps_advance: number of timesteps between current t and closest previous timestep to be included
n_timesteps_window: length in timesteps of window to be included 

e.g. n_timesteps_window=3 and n_timesteps_advance=1, then variable of interest at t-1, t-2, t-3 appended to each row 
e.g. n_timesteps_window=2 and n_timesteps_advance=3, then variable of interest at t-3 and t-4 appended to each row

'''

import numpy as np

def append_history(df,var,n_timesteps_advance,n_timesteps_window):

# need to do this for range function
#n_timesteps_window += 1

	for k in range(n_timesteps_advance,n_timesteps_advance+n_timesteps_window):
		
		df['%s_t-%i'%(var,k)] = np.zeros(len(df[var]))
    
       
	for i in range(n_timesteps_advance+n_timesteps_window,len(df[var])):

		for j in range(n_timesteps_advance,n_timesteps_advance+n_timesteps_window):

			df['%s_t-%i'%(var,j)][i] = df[var][i-j]

		df['%s_t-%i'%(var,j)] = 

	df = df.ix[n_timesteps_advance+n_timesteps_window:]
       
	return df

def append_history_diff(df,var,):
	
	return df

	