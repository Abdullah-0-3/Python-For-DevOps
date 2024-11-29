# Calculate Area and Circumference of Circle

import math

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

radius = float(input("Enter radius of circle: "))
print("Area of circle is: ", area(radius))
print("Circumference of circle is: ", circumference(radius))