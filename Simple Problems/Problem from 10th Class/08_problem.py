# Calculate Sum of 5 Subjects and find Percentage

def percentage():
    # Input from User
    sub1 = int(input("Enter Marks of Subject 1: "))
    sub2 = int(input("Enter Marks of Subject 2: "))
    sub3 = int(input("Enter Marks of Subject 3: "))
    sub4 = int(input("Enter Marks of Subject 4: "))
    sub5 = int(input("Enter Marks of Subject 5: "))

    sum = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = ((sum / 5) / 100) * 100
    print("Total Marks: ", sum)
    print(f"Percentage: {percentage}%")

percentage()