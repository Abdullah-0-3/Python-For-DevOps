with open("logs.txt", "r") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes, Python is present")
    count = content.lower().count('python')
    print(f"Python is present {count} times")
else:
    print("No, Python is not present")