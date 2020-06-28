l = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    numbers = int(input())
    l.append(numbers)

def unique(l):
    return(list(set(l)))

print(unique(l))
