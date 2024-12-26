# List Comprehension

numbers = [1, 2, 3, 4, 5]

# Before List Comprehension
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print(squared_numbers)

# List Comprehension
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)