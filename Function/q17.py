string = input('enter the string :')
char = input('enter the char: ')

check = lambda x: True if x.startswith(char) else False

print(check(string))