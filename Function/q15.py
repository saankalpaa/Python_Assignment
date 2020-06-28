l = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    l.append(numbers)

even = list(filter(lambda x: x%2 == 0, l))

print(even)