import sys, math
import matplotlib.pyplot as plt

x = []
y = []

fd = open('ranks.txt', 'r')
for line in fd.readlines():
	line = line.strip()
	if line == '':
			continue
	
	row = line.split('\t')
	x.append(math.log(int(row[0])))
	y.append(math.log(int(row[1])))

plt.plot(x, y, 'ro')
plt.show()