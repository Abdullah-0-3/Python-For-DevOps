from functools import reduce
numbers = [i for i in range(1, 1001)]

def greater_than(n, g):
    if n > g:
        return n
    return g

print(reduce(greater_than, numbers))