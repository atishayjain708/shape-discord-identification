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