list = []
n = int(input("enter the no. of words you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list.append(words)

def func(list):
    count = 0
    for i in range(0,n):
        str =list[i]
        if len(str) >= 2 and str[0]==str[-1:]:
            count += 1 
        else:
            pass
    return count

print('count :',func(list))

