def insert_str(string, word):
	return string[:2] + word + string[2:]
print(insert_str('[[]]', 'Python'))
print(insert_str('{{}}', 'PHP'))