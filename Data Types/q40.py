tuple = 4,16,64
print('Before adding items: ',tuple)
n= int(input('enter the no. of items you want to add in tuple: '))

for i in range(0,n):
    item = int(input())
    tuple = tuple + (item,)
    
print('After adding items: ',tuple)

