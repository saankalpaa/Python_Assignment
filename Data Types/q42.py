list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    items = input()
    list.append(items)
print('list: ',list)

def convert_list(list):
    return tuple(list)

print('tuple: ',convert_list(list))