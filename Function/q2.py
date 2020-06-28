list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    list.append(numbers)

def add_num(list):
    sum = 0
    for i in range(0,n):
        sum = sum + list[i]
    return sum

print('sum of all the numbers in the list = ',add_num(list))