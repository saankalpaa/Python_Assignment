string = input('enter the string: ')


def count(string):
    u = 0
    l = 0
    for i in string:
        if i.isupper():
            u += 1
        else:
            l += 1
    print('No. of Upper case char: %s' % str(u))
    print('No. of Upper case char: %s' % str(l))


count(string)

