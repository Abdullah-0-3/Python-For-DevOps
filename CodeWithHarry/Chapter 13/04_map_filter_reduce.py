# Map Filter Reduce

# Map

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x: x * x

sq_list = map(square, l)
print(list(sq_list))

# Filter
def even(num):
    if num % 2 == 0:
        return True
    return False

only_even = filter(even, l)
print(list(only_even))

# Reduce
from functools import reduce
sum = lambda x, y: x + y

print(reduce(sum, l))

'''
Reduce Function works like this

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
15 + 6 = 21
21 + 7 = 28
28 + 8 = 36
36 + 9 = 45
45 + 10 = 55
'''