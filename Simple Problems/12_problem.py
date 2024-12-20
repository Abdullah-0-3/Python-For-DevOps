# Finding Number is Positive, Negative or Zero

def pos_neg_zero(num):
    if num == 0: 
        print("Number is Zero -", num)
    elif num > 0:
        print("Number is Positive - +" + str(num))
    else: 
        print("Number is Negative - " + str(num))

if __name__ == '__main__':
    num = int(input("Enter any Number: "))
    pos_neg_zero(num)