# Problem 04    

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"{a} / {b} = {a/b}")
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Error: ", e)