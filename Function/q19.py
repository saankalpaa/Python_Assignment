from functools import reduce
n = int(input('enter the value of n: '))
fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

print(fibonacci(n))