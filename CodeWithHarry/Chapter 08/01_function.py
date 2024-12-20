# Function 

'''
function is a block of code that only runs when it is called.
You can pass data, known as parameters, into a function.
'''

# Faltu Way
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

average = (a + b + c) / 3
print(average)
'''

def average():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    average = (a + b + c) / 3
    print(average)

def line():
    for i in range(10):
        print("")
        print("*", end=" ")
02
average()
line()