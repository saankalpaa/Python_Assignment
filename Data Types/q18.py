list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    items = int(input())
    list.append(items)

def largest(list):
    largest = list[0]
    for i in range(0,n):
        if largest < list[i]:
            largest = list[i]
        else:
            pass
    return largest

print('list: ',list)
print('Largest number from the list is : ',largest(list))
