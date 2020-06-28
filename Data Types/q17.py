list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    items = int(input())
    list.append(items)

def multiply(list):
    product = 1
    for i in range(0,n):
        product = product * list[i]
    return product

print('list: ',list)
print('product = ',multiply(list))
