marks = {
    "Abdullah": 90,
    "Ali": 80,
    "Ahmed": 70,
    "Ahsan": 60,
    "Aamir": 50
}

print(marks)
print(type(marks))

# Accessing the value of a key
print(marks["Abdullah"])

# Adding a new key-value pair
marks["Asad"] = 40
print(marks)

# Deleting a key-value pair
del marks["Asad"]
print(marks)

# Updating a value of a key
marks["Ali"] = 85
print(marks)

# Getting all the keys
print(marks.keys())

# Getting all the values
print(marks.values())