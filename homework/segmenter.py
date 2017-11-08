import sys


for line in sys.stdin.readlines(): 
	line = line.replace('.', '.\n')
	print(line)