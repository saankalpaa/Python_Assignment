list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list.append(words)

new_list =[]
n = int(input("enter the no. of items you want to replace with the end of the previous list :  "))
for i in range(0,n):
    words = input()
    new_list.append(words)

list[-1:] = new_list
print(list)
    
