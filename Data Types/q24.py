list_a = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    list_a.append(words)

list_b = list_a.copy()
print("original_list: ", list_a)
print("copied list:   ", list_b)