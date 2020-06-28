string=input('enter the string')

def add(string):
    n= len(string)
    if n >= 3:
        if string[-3:] == 'ing':
            string = string + 'ly'
        else:
            string = string + 'ing'
    else:
        pass
    return(string)

print(add(string))  
