# Question 10

# Reverse Order Table

n = int(input("Enter a number: "))
ending = int(input("Enter the ending number: "))

for i in range(ending, 0, -1):
    print(f"{n} * {i} = {n * i}")

