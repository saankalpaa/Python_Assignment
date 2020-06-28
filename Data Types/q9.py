string = input('enter the string')

def change(string):
    string = string[-1:] + string[1:-1] + string[0]
    return string

print(change(string))
