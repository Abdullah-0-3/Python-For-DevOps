# Taking input for three subjects
subject_1 = int(input("Enter the first subject: "))
subject_2 = int(input("Enter the second subject: "))
subject_3 = int(input("Enter the third subject: "))

# Checking for Total Percentage
total = subject_1 + subject_2 + subject_3

percentage = (total / 300) * 100  
print(f"The total percentage is: {percentage:.2f}%") 

condition = subject_1 >= 33 and subject_2 >= 33 and subject_3 >= 33

if (percentage >= 40 and condition):
    print("Congratulations! You have passed")
else:
    print("Sorry! You have failed")