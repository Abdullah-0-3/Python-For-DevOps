age = int(input("Enter your age: "))

if (age >= 18):
    print("You are above the age of consent.")
    print("Good for you!")
elif (age < 0):
    print("You are not born yet :)")
elif (age == 0):
    print("You are a baby.")
else:
    print("You are below the age of consent.")