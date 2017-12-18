import sys 

s = sys.stdin.readlines()

vocab = {}
freqlst = {}
tag_frequency = {}
freq = []
tags_freq = []
count = 0

for line in s:
	if '\t' not in line:
		continue
	row = line.split('\t')
	form = row[1].strip()
	tag = row[4].strip()
	if form not in vocab:
		vocab[form] = tag
	if tag not in tag_frequency:
		tag_frequency[tag] = 0
	tag_frequency[tag] = tag_frequency[tag] + 1
	if form not in freqlst:
		freqlst[form] = 0
	freqlst[form] = freqlst[form] + 1
	count = count +1

for t in tag_frequency:
	tags_freq.append((tag_frequency[t], t))
tags_freq.sort(reverse=True)

for f in freqlst:
	freq.append((freqlst[f], f))

freq.sort(reverse=True)

fd = open('model.tsv', 'w+')
fd.write('# P' + '\t' + 'count' + '\t' + 'tag' + '\t' + 'form' + '\n')

for i in tags_freq:
	c = i[0] / count
	c = str(round(c, 4))
	fd.write(c + '\t' + str(i[0]) + '\t' + i[1] + '\t' + '-' + '\n')

for item in freq:
	if item[1] in vocab:
		a = item[1]
		d = item[0] / item [0]
		fd.write(str(d) + '\t' + str(item[0]) + '\t' + vocab[a] + '\t' + a + '\n')
fd.close()
#The problem is that I did not manage to count the number of pairs 
#(and I am not sure there is a need to do so, if we are using dictionaries...)
#so that's a bad and stupid solution, 
#but as far as I understand, there is no possibility to have two values for the same key
#that's why I kind of exclude this possibility
 # :((
