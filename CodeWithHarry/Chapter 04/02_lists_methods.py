# Lists Method

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(dir(friends))

# Joined at the end of the list
friends.append("Creed")
print(friends)

# Sort the list
friends.sort()
print(friends)

# Reverse the list
friends.reverse()
print(friends)

# Insert at a specific index
friends.insert(1, "Kelly")
print(friends)

# Remove a specific element
friends.remove("Jim")
print(friends)

# Remove the last element
friends.pop()
print(friends)

# Check if an element is in the list
print(friends.index("Oscar"))

# Count the number of times an element appears in the list
print(friends.count("Jim"))