import csv
import sys
import math
import numpy as np

from saxpy.znorm import znorm

def dist(a, b):
	return np.sqrt(np.sum((a-b)**2))

def get_dist(S, m, n):
	dist_matrix = np.zeros((m,m) , dtype=float)
	dist_array = np.zeros(n,float)
	for i in range(0,m):
		for j in range(i+1,m):
			for k in range(0,n):
				dist_array[k] = dist(S[i],np.roll(S[j],k))
			dist_matrix[i][j] = min(dist_array)
			dist_matrix[j][i] = dist_matrix[i][j]
	return dist_matrix

best_so_far_dist = 0
best_so_far_index = -1
Outer = []
Inner = []
m = int(input('Enter no. of shapes in time series.'))
n = int(input('Enter length of time series.'))
with open('heuristics'+sys.argv[1]+'.txt', 'r') as h:
	outer_line = h.readline().strip().split(' ')
	inner_line = h.readline().strip().split(' ')
	for i in outer_line:
		Outer.append(int(i))
	for i in inner_line:
		Inner.append(int(i))

S = []
with open('DATA/'+sys.argv[1], newline='') as test_file:
	lines = csv.reader(test_file)
	for line in lines: 					# every line is a list of strings
		# del line[0] 					# remove 1st element as it is the class (TODO - pop this into a separate array)
		data = np.array(line) 			# every line/row in the file as a np string array
		data = np.asfarray(data,float) 	# converted to np float array
		data_znorm = znorm(data)
		S.append(data_znorm)
dist_matrix = get_dist(S,m,n)

line_count = 0
for p in Outer:
	C = S[p]					# C represents the current time series being worked upon
	nearest_neighbor_dist = math.inf
	for q in Inner:
		if p != q:
			D = dist_matrix[p,q]
			flag = 0
			if D < best_so_far_dist:
				flag = 1
				break
			if D < nearest_neighbor_dist:
				nearest_neighbor_dist = D
	# print('inner loop done.\n')
	if nearest_neighbor_dist > best_so_far_dist and flag != 1:
		best_so_far_dist = nearest_neighbor_dist
		best_so_far_index = p
	line_count+=1

with open ('results' , 'a+') as r:
	r.write(sys.argv[1]+'\t'+str(best_so_far_dist)+'\t'+str(best_so_far_index)+'\n')

print((best_so_far_index,best_so_far_dist))