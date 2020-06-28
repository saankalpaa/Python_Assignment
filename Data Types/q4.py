str1 = input('enter the first string')
str2 = input('enter the second string')

def swap(str1,str2):
    string = str2[0:2] + str1[-1:] + ' ' + str1[0:2] + str2[-1:] 
    return(string)

print(swap(str1,str2))
