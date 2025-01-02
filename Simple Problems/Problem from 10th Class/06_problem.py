# Calculate Area of Right Angle Triangle

def area(base, height):
    return 0.5 * base * height

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of right angle triangle is: ", area(base, height))