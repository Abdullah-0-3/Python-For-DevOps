with open('rename.txt', 'r') as f:
    data = f.read()
    print(data)

with open('rename_python.txt', 'w') as f:
    f.write(data)