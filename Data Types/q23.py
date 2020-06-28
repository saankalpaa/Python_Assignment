l = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    l.append(words)

if not l:
    print("List is empty")
else:
    print("list is not empty\n")
    print("list: ",l)