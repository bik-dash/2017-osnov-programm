import sys

s = sys.stdin.readlines()
s1 = sys.stdin.read()

n_lines = 0
n_tokens = 0
n_chars = 0

for line in s:
	print(line)
	n_lines = n_lines + 1
	tokens = line.strip(' ')
	for token in tokens:
		n_tokens = n_tokens + 1
	for char in line:
		n_chars = n_chars + 1

print("The number of lines:", n_lines)
print("The number of words:", n_tokens)
print("The number of characters:", n_chars)
