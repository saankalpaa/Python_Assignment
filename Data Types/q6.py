string=input('enter the string')

def find(string):
    str1 = string.find('not')
    str2 = string.find('poor')

    if str1<str2 and str1>0 and str2>0:
        string = string.replace(string[str1:(str2+4)],'good')
        return string
    else:
        return string

print(find(string))
