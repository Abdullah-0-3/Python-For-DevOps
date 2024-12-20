# Question 5

names = ["Abdullah", "Ali", "Muhammad", "Ahmed", "Usman", "Ayesha", "Aisha", "Fatima", "Zainab", "Khadija"]

name = input("Enter your name: ")
name = name.capitalize()

if name in names:
    print("Your name is found in the list")
else:
    print("Your name is not found in the list")