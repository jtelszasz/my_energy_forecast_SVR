
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.plotly as py
from plotly.graph_objs import *

import import_funcs

def main():

	plotly_name = 'My Electricity Use Visualizations/Heatmap Daily by Week'
	
	new_apt = import_funcs.BGEdata("new apt")


	daily_totals = pd.DataFrame(np.zeros([len(new_apt['USAGE'].resample('W-MON', how='sum')),7]),
                            index = new_apt['USAGE'].resample('W-MON', how='sum').index)

	# Drop the last two rows to ensure each row is a full week
	daily_totals = pd.DataFrame(np.zeros([len(new_apt['USAGE'].resample('W-MON', how='sum')),7]),
	                            index = new_apt['USAGE'].resample('W-MON', how='sum').index)

	daily_totals.drop(daily_totals.tail(2).index, inplace=True)

	for j in range(len(daily_totals)):
	    for i in range(7):
	        #print i, j
	        daily_totals[i].ix[j] = new_apt['USAGE'].resample('D', how='sum').ix[(daily_totals.ix[j].name + pd.to_timedelta(i, unit='d'))]

	daily_totals.columns = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']

	daily_totals.sort_index(ascending=False, inplace=True)

	data = Data([
	    Heatmap(
	        y = daily_totals.columns,
	        x = daily_totals.index,
	        z = np.transpose(np.array(daily_totals)),
	        colorscale='YIOrRd',
	        reversescale=True,
	        colorbar = ColorBar(
	        	title = 'Kilowatt-Hours',
        		titleside='right'
        	)
	    )
	])

	layout = Layout(
	    yaxis = YAxis(tickangle=0),
	    autosize = False,
	    width = 800,
	    height = 300,
	    margin=Margin(
	        l=50,
	        r=50,
	        b=50,
	        t=50,
	        pad=4
	    )
	)

	#plot_url = py.plot(data, layout=layout, filename='Daily_Totals_by_Week')
	fig = Figure(data=data, layout=layout)
	py.iplot(fig, filename=plotly_name)
	
	print "Sent to Plotly: ", plotly_name

if __name__ == "__main__":
	main()
