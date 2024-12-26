# Try and Else block

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except Exception as e:
    print(f"Error:", e)
else: 
    print("No exception occurred")