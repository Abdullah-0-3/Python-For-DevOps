# Problem 03

num = int(input("Enter a number: "))

table = [num * i for i in range(1, 13)]

for i, item in enumerate(table):
    print(f"{num} * {i+1} = {item}")