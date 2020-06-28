array_1 = [1, 6, 9, 10, 11, 14]
array_2 = [7, 9, 10, 14, 18]
intersect = list(filter(lambda x: x in array_1, array_2))

print(intersect)