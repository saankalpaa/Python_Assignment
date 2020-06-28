d = {'item_1':10,'item_2':33,'item_3':2}
product = 1
for item, value in d.items():
    product = product * d[item]
print(product)