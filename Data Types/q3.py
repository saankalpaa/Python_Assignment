str1 = input('enter the string')

def func(str1):

    char = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char + str1[1:]
    return str1

print(func(str1))
          
        
           