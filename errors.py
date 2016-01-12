'''
errors.py

Created by Justin Elszasz, 5.15.2014

errors.calc_RMSE(y,t) - calculates root mean square error
errors.calc_MAPE(y,t) - calculates average predicted error
errors.calc_CV(y,t) - calculates coefficient of variation
errors.calc_MBE(y,t) - calculates mean bias error

Calculates error measures for predictive models

y: Pandas dataframe of predicted values (one column)
t: Pandas dataframe of target values (one column)

'''

import pandas as pd
import numpy as np

def calc_RMSE(y,t):

	N_test = len(y)
	if N_test != len(t):
		raise Exception, 'Length of predicted values does not equal length of target values.'
	
	RMSE = pow(pow(t-y,2).sum()/N_test,.5)
	return RMSE

def calc_MAPE(y,t):

	N_test = len(y)
	if N_test != len(t):
		raise Exception, 'Length of predicted values does not equal length of target values.'

	MAPE = ((t-y).abs()/y).sum()/N_test
	return MAPE

def calc_MBE(y,t):
	
	N_test = len(y)
	if N_test != len(t):
		raise Exception, 'Length of predicted values does not equal length of target values.'

	MBE = (t-y).sum()/(N_test-1)/t.mean()
	return MBE

def calc_CV(y,t):

	N_test = len(y)
	if N_test != len(t):
		raise Exception, 'Length of predicted values does not equal length of target values.'

	CV = pow(pow(t-y,2).sum()/(N_test-1),.5)/t.mean()
	return CV