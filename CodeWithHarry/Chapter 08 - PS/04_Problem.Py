# Question 04

def sum_natural_numbers(n):
    if n < 1:
        return 0
    else:
        return sum_natural_numbers(n - 1) + n

n = int(input("Enter the number: "))
print(f"The sum of first {n} natural numbers is {sum_natural_numbers(n)}")