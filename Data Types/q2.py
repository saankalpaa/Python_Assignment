str = input('enter the string')

def func(str):
    if len(str)>=2:
        return str[0:2] +str[-2:]
    else:
        return 'empty string'

print(func(str))
