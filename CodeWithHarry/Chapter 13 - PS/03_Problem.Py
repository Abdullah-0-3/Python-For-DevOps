def divisible_5(n):
    if n % 5 == 0:
        return True
    return False

numbers = [i for i in range(1, 1001)]

divisible_5_numbers = list(filter(divisible_5, numbers))
print(divisible_5_numbers)