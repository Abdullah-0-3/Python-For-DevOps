# Question 6

'''
Factorial of a number
Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Write a program that asks the user for a number and then prints the factorial of that number.
'''

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")


# Whie loop
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print(f"The factorial of {num} is {factorial}")