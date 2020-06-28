list = []
n = int(input("enter the no. of words you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list.append(words)

def func(list):
    max_length = len(list[0])
    for i in range(0,n):
        length = len(list[i])
        if max_length < length:
            max_length = length
        else:
            pass
    return(max_length)

print('The length of the longest one is :',func(list))

