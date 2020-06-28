string = input('enter the string: ')

check = lambda x: True if x.isnumeric() else False

print(check(string))