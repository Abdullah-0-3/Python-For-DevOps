# Question 06

def inch_to_cm(inch):
    cm = inch * 2.54
    return cm

inch = float(input("Enter the length in inches: "))
print(f"The length in centimeters is {inch_to_cm(inch)}")