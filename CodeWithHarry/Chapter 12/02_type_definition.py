# Type Definition

'''
You can define a new type by using the class keyword.
It can be a good idea to define a new type when you want to add some methods to it.
'''

n : int = 10
print(n)

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

'''
The Function says:
1. a value is integer
2. b value is integer
3. return value is integer
'''