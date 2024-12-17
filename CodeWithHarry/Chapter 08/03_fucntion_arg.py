# Funciton Arugments

# 1. Positional Arguments
def add(a, b):
    return a + b

print(add(2, 3))

# 2. Keyword Arguments
def add(a, b):
    return a + b

print(add(b=2, a=3))

# 3. Default Arguments
def add(a, b=3):
    return a + b

print(add(2))

# 4. Variable-length Arguments
def add(*args):
    return sum(args)

print(add(2, 3, 4, 5, 6, 7, 8, 9, 10))

# 5. Keyword Variable-length Arguments
def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person(first_name="Shahriar", last_name="Shakil", age=24, city="Dhaka")

# 6. Docstring
def add(a, b):
    '''This function takes two arguments and returns their sum.'''
    return a + b

print(add.__doc__)

# 7. Scope
x = 5

def func():
    x = 7
    return x

print(x)