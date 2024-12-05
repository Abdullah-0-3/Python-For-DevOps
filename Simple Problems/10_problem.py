# Compare theree Integers

def three_integers(a, b, c):
    if a > b and a > c:
        print('A is Greater -', a)
    elif b > a and b > c:
        print("B is Greater -", b)
    elif c > a and c > b:
        print("C is Greater -", c)
    else:
        print("All are Equal")

if __name__ == "__main__":
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    c= int(input("Enter third Number: "))
    three_integers(a, b, c)