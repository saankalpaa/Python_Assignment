list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    items = int(input())
    list.append(items)

def smallest(list):
    smallest = list[0]
    for i in range(0,n):
        if smallest > list[i]:
            smallest = list[i]
        else:
            pass
    return smallest

print('list: ',list)
print('smallest number from the list is : ',smallest(list))
