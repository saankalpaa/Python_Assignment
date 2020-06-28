my_list = []
n = int(input("enter the no. of items you want to add in the list :  "))
for i in range(0,n):
    words = input()
    my_list.append(words)

def remove_dup(my_list):
    my_list = list(dict.fromkeys(my_list))
    return my_list

print(remove_dup(my_list))