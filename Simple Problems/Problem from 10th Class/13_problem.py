# Swap two numbers using variable named temp

def swap(a, b):
    print(f"a is {a} and b is {b}")
    temp = a
    a = b
    b = temp
    print(f"Now, a is {a} and b is {b}")

if __name__ == "__main__":
    swap(4, 5)