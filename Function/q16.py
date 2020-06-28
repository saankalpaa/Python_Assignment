l = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    l.append(numbers)

square = list(map(lambda x: x**2, l))
print(square)

cube = list(map(lambda x: x**3, l))
print(cube)