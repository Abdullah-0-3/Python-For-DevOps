# Enumerate Function

''' Before Enumerate Function
index = 0
for fruit in fruits:
    print(f"Fruit {index}: {fruit}")
    index += 1
'''

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Fruit {index}: {fruit}")