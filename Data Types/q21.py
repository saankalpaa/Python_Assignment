
def arrange(data): 
    return data[1]

def sort_list(tuples):
  return sorted(tuples, key=arrange)

print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
