list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    list.append(numbers)

def multiply(list):
    product = 1
    for i in range(0,n):
        product = product * list[i]
    return product

print('product of all the numbers in the list = ',multiply(list))