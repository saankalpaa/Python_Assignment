list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list.append(words)

result = all(list)
print(result)