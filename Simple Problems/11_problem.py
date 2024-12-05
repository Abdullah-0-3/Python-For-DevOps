# Number is Even or Odd

def even_odd(num):
    if num % 2 == 0:
        print("Number is Even -", num)
    else: 
        print("Number is Odd -", num)

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    even_odd(num)