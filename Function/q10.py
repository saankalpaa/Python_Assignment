l = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    l.append(numbers)

def even(x):
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(even(l))

