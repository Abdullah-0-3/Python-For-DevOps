marks = {
    "Abdullah": 90,
    "Ali": 80,
    "Ahmed": 70,
    "Ahsan": 60,
    "Aamir": 50
}

print(marks.items())

print(marks.keys())

print(marks.values())

print(marks.get("Ali"))

marks.update({"Ali": 85, "Asad": 75})
print(marks)

# Difference

print(marks.get("Ali"))
print(marks["Ali"])

'''
The get() method returns the value of the item with the specified key.
The difference between get() and [] operator is that get() method returns None if the key is not found.
'''