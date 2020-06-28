list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    items = int(input())
    list.append(items)

def add(list):
    sum = 0
    for i in range(0,n):
        sum = sum + list[i]
    return sum

print('list: ',list)
print('sum = ',add(list))
