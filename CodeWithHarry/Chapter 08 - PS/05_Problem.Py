# Question 05

'''
Pattern

***
**
*
'''

# Simple
def lines(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter the number of lines: "))
lines(n)

# Recursion
def lines(n):
    if n == 0:
        return
    print("*" * n)
    lines(n - 1)

n = int(input("Enter the number of lines: "))
lines(n)