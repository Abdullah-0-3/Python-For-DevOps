# Recursion 

'''
Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.
'''

# Example 1: Factorial
def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        fact =  n * factorial(n-1)
        return fact

n = int(input("Enter a number: "))
print(factorial(n))

# Example 2: Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i), end=" ")

# Example 3: Sum of n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)

n = int(input("Enter a number: "))
print(sum_natural(n))