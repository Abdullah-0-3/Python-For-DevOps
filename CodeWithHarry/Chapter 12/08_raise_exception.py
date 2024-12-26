num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = num1 / num2
except ZeroDivisionError as e:
    print(e)
else:
    print(f"Result: {result}")