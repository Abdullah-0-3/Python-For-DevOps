# Try and Finally block

def with_finally():
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
    except Exception as e:
        print(f"Error:", e)
    finally:
        print("Finally block executed")

with_finally()

def without_finally():
    try:
        num = int(input("Enter a number: "))
        return print(f"You entered: {num}")
    except Exception as e:
        print(f"Error:", e)
    print("Without Finally block executed")

without_finally()