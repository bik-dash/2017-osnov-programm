import sys

s = sys.stdin.readlines()

tr = {'а' : 'a', 'б' : 'b', 'в' : 'v', 'г' : 'g', 'д' : 'd', 'е' : 'e', ' е' : ' je', 
'ё' : 'jo', 'ж' : 'zh', 'з' : 'z', 'и' : 'i', 'й' : 'j', 'к' : 'k',  'л' : 'l', 'м' : 'm', 
'н' : 'n', 'о' : 'o', 'п' : 'p', 'р' : 'r', 'с' : 's', 'т' : 't', 'у' : 'u', 'ф' : 'f', 
'х' : 'kh', 'ц' : 'ts', 'ч' : 'ch', 'ш' :'sh', 'щ' : 'sch', 'ъ' : 'j', 'ы' : 'y', 
'ь' : 'j', 'э' : 'e', ' ю' : 'ju', 'я' : 'ja', 'А' : 'A', 'Б' : 'B', 'В' : 'V', 'Г' : 'G',
 'Д' : 'D', 'Е' : 'Je', 'Ё' : 'Jo', 'Ж' : 'Zh', 'З' : 'Z', 'И' : 'I',  'Й' : 'J', 
'К' : 'K', 'Л' : 'L', 'М' : 'M', 'Н' : 'N', 'О' : 'O', 'П' : 'P', 'Р' : 'R', 
'С' : 'S', 'Т' : 'T', 'У' : 'U', 'Ф' : 'F', 'Х' : 'H', 'Ц' : 'Ts', 'Ч' : 'Ch', 
'Ш' : 'Sh', 'Щ' : 'Sch', 'Ы' : 'Y', 'Э' : 'E', 'Ю' : 'Ju', 'Я' : 'Ja'}

for line in s:
	converted_line = ''
	for char in line:
		transchar = ''
		if char in tr:
			transchar = tr[char]
		else:
			transchar = char
		converted_line += transchar
	print(converted_line)		
	