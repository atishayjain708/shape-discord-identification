# n = 251
# Using no. of alphabets = 20 and w = 4
import sys
import csv
import numpy as np
import saxpy.discord as discord
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize

from itertools import permutations
from collections import defaultdict

sax_words = []

with open('DATA/'+sys.argv[1], 'r') as h:
	lines = h.readlines()
	for line in lines:
		line = line.strip().split(',')
		data = []
		for num in line:
			if num.strip() != '':
				data.append(float(num.strip()))
		data_znorm = znorm(data)
		data_paa = paa (data_znorm, 4)
		sax_words.append(ts_to_string(data_paa, cuts_for_asize(20)))


sax_words_ri = []
i = 0
for word in sax_words:
	perms = set([''.join(p) for p in permutations(word)])
	sax_words_ri.append(perms)
	i+=1

#Write all SAX words to file only once instead of generating again and again
with open('sax_words_ri_all_Lshifts.txt', 'w+') as sax_words_file:
	for lis in sax_words_ri:
		for l in lis: 
			sax_words_file.write(l+' ')
		sax_words_file.write('\n')