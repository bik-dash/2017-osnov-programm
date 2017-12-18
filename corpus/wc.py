import sys

l = 0
t = 0
ch = 0
vowels = 0

for c in sys.stdin.read():
	if c == ' ':
		t = t+1
	if c == '\n':
		l = l+1
	ch = ch+1
	if c in 'иуэоаеёыюя':
		vowels = vowels +1
print(l,t,ch,vowels, vowels/t, ch/t) 
