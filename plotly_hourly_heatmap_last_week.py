
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.plotly as py
from plotly.graph_objs import *

import import_funcs

def main():

	plotly_name = 'My Electricity Use Visualizations/Heatmap Hourly Last Week'

	new_apt = import_funcs.BGEdata("new apt")
	last_week = pd.DataFrame(new_apt['USAGE'].ix[new_apt['USAGE'].index.week == new_apt['USAGE'].index[-1].week])

	# Change this if not a full week at end of month!!
	week_index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']

	# Change size of dataframe if not a full week at end of month!!
	last_week_array = pd.DataFrame(np.zeros([6,24]))

	# Build array for last week
	for i in range(24):
	    last_week_array[i] = np.array(last_week[last_week.index.hour==i])
	last_week_array.index = week_index


	data = Data([
	    Heatmap(
	        x = range(0,24,1),
	        y = last_week_array.index,
	        z = np.array(last_week_array),
	        colorscale='YIGnBu',
	        reversescale=True)
	])

	layout = Layout(
	    title='Week of %s <br>'%last_week.ix[0].name.strftime('%B %d, %Y'),
	    yaxis = YAxis(autorange='reversed')
	)
	#plot_url = py.plot(data, filename='Last Week Heat Map')
	fig = Figure(data=data, layout=layout)
	py.iplot(fig, filename=plotly_name)

	print "Sent to Plotly: ", plotly_name

if __name__ == "__main__":
	main()