a = 10
b = 30
c = 50

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

env = "prod"
if env == "prod":
    print("You are in production environment")
else:
    print("You are in development environment")

# Fuction

def check_biggest(a, b, c):
    if a > b and a > c:
        print("a is greater")
    elif b > a and b > c:
        print("b is greater")
    else:
        print("c is greater")
    return a, b, c

check_biggest(10, 20, 30)