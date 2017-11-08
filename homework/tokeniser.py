import sys

sent_id = 1

s = sys.stdin.readlines()
for line in s:
	line = line.strip()
	if line == '':
		continue
	print('# sent_id = ', sent_id)
	print('#text = ', line)
	line = line.replace('.', ' .')
	line = line.replace(',', ' ,')
	line = line.replace('(', '( ')
	line = line.replace(')', ' )')
	line = line.replace(':', ' :')
	line = line.replace(';', ' ;')
	line = line.replace('!', ' !')
	line = line.replace('?', ' ?')
	line = line.replace('"', ' " ')
	
	sent_id = sent_id + 1
	token_id = 1
		
	tokens = line.split(' ')
	for token in tokens:
		print(token_id, '\t', token, '\t_\t_\t_\t_\t_\t_\t_\t_')
		token_id = token_id + 1
	print()