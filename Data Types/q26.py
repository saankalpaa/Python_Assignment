list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list.append(words)

def insert(list):
    new_list =  ['emp{0}'.format(i) for i in  list]       
    return new_list

print(insert(list))

