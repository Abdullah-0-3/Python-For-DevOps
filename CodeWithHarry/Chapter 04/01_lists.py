# List

'''
List is a collection which is ordered and changeable. Allows duplicate members.
In Python lists are written with square brackets.
Lists are used to store multiple items in a single variable.
Lists are immutable, meaning that the elements inside a list can be changed.
'''

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[1])

friends[1] = "Mike"
print(friends)

print(friends[1:3])