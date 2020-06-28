string = input('enter the string: ')
n = int(input('enter the index: '))
def remove(string, index):
    string = string[:n] + string[n+1:]
    return string

print('string after the removal of specified index char: ',remove(string, n))