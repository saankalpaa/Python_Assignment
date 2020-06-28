tuplex = "a", 3, "b", "c", "d", "e"
print('Before removal of item,tuple: ',tuplex)
#converting the tuple to list
listx = list(tuplex) 
listx.remove(3) 
#converting the list to tuple
tuplex = tuple(listx)
print('After removal of item,tuple: ',tuplex)
