# Printing table of a Number

def table(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    table(num)