# Question 1

def greater(a, b, c):
    if ((a > b) and (a > c)):
        msg = f"{a} is greater"
        return msg
    elif ((b > a) and (b > c)):
        msg = f"{b} is greater"
        return msg
    else:
        msg = f"{c} is greater"
        return msg

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(greater(a, b, c))