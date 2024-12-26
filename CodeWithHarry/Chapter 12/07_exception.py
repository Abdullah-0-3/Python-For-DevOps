# Exception Handling

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Please enter a number greater than 0")
except Exception as e:
    print(f"Error: {e}")

print("Program Ended")