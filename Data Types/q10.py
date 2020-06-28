string = input('enter the string')

def remove(string):
    n = len(string) 
    s = ""
    for i in range(0,n):
        if i % 2 == 0:
            s = s + string[i]
    return s

print(remove(string))