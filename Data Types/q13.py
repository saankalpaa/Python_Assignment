elements = input('enter the sequence of words separated by comma: ')

def func(elements):
    words = [word for word in elements.split(",")]
    sort = words.sort()
    items = (",".join(words))
    return items

print(func(elements))