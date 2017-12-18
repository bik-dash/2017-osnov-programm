import sys

s = sys.stdin.readlines()
m = sys.argv[1]

default_tag = 'NOUN'
words = {}

fd = open(m, 'r')
for line in fd.readlines():
	if '\t' not in line:
		continue
	row = line.strip().split()
	t = row[3]
	tag = (row[2], row[0])
	if t == '_':
		default_tag = max(default_tag, tag, key = lambda x: x[1])
	else:
		if t not in words:
			words[t] = tag
		else:
			words[t] = max(words[t], tag, key = lambda x: x[1])

fd1 = open('tagger_result.txt', 'w')
for line in s:
	if '\t' not in line:
		fd1.write('\n')
		fd1.write(line)
	else:
		row = line.strip().split()
		w = row[1]
		if row:
			if w in words:
				tag = words[w][0]
			else:
				tag = default_tag[0]
			row[3] = tag
			fd1.write('\t'.join(row) + '\n')
fd1.close()