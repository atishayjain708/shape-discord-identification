from string import ascii_lowercase
def find_min_max_alpha(fileName):
	with open(fileName, 'r') as f:
		U = ascii_lowercase[0]
		L = ascii_lowercase[25]
		while True:
			c = f.read(1)
			if not c:
				break
			if c == ' ' or c == '\n':
				continue
			if c<L:
				L=c
			if c>U:
				U=c
		return (L,U)

limits = find_min_max_alpha('sax_words_ri_all_Lshifts')
string = ascii_lowercase[ascii_lowercase.index(limits[0]):ascii_lowercase.index(limits[1])]
buffer = []
with open('buckets', 'w+') as b:
	for i in string:
		for j in string:
			buffer.append(i+j)
	set(buffer)
	sorted(buffer)
	for bucket in buffer:
		b.write(bucket+'\t')
		n=ord(bucket[0])+ord(bucket[1])
		b.write(str(n))
		b.write('\n')




    	
