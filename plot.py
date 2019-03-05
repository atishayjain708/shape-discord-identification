# Make sure the file you are trying to plot exists in the folder /DATA/.
# Enter name of the data-set you wish to plot.
# In case you wish to plot one specific time-series (or the time-seres for a specific image) enter the index of that time series. This menu option will be helpful when trying to verify the results from our algorithm. (i.e. index will be picked up from the results file in the root directory).   

import matplotlib.pyplot as plt
import csv
import sys
import numpy as np

if sys.argv[1] != '':
	dataset = sys.argv[1]
else:
	dataset = input('Enter name of data-set:\n')
if sys.argv[2] != '':
	index_to_plot = sys.argv[2]
else:
	index_to_plot = input('Enter the index of time series you wish to plot (0-indexed)\nEnter \'a\' to plot all time series:\n')
with open('DATA/'+ dataset,'r') as csvfile:
    all_series = csv.reader(csvfile, delimiter=',')
    cur_index = 0
    for series in all_series:  	
    	if index_to_plot == 'a':
    		del series[0]
    		data = np.asfarray(series)
    		plt.plot(data, label=str(cur_index))
    	elif cur_index == int(index_to_plot):
    		del series[0]
    		data = np.asfarray(series)
    		plt.plot(data, label=str(cur_index))
    		break
    	cur_index+=1
plt.legend()
plt.show()