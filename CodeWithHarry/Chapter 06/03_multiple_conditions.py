# Multiple Conditonal Statements

age = int(input("Enter your age: "))

if (age % 2 == 0):
    print("Your age is an even number.")
else:
    print("Your age is an odd number.")

if (age >= 18):
    print("You are above the age of consent.")
    print("Good for you!")
    if (age >= 60):
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are below the age of consent.")
    if (age < 0):
        print("You are not born yet :)")
    elif (age == 0):
        print("You are a baby.")
    else:
        print("You are a child.")