# Tuple

'''
Tuple is a collection of items which is ordered and unchangeable.
In Python tuples are written with round brackets.
Tuples are used to store multiple items in a single variable.
Tuples are immutable, meaning that the elements inside a tuple can't be changed.
'''

countries = ("India", "USA", "UK", "Canada", "Australia")
print(type(countries))
print(countries)

# If you try to change the value of a tuple, you will get an error
countries[1] = "Germany"
print(countries)

# You can't remove items from a tuple
del countries[1]
print(countries)

# You can delete the entire tuple
del countries
print(countries)

# You can't change the entire tuple
countries = ("India", "USA", "UK", "Canada", "Australia")
countries = ("India", "USA", "UK", "Canada", "Australia", "Germany")
print(countries)