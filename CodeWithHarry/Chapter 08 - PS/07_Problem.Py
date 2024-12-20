# Question 07

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def remove_fruit(fruit, word):
    n = []
    for item in fruit:
        if not(item == word):
            n.append(item.strip(word))
    return n

word = input("Enter the word to remove: ")
print(remove_fruit(fruits, word))