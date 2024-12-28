# Probem 01

def format():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    phone_no = int(input("Enter your phone number: "))

    print("Name: {0} \nMarks: {1} \nPhone Number: {2}".format(name, marks, phone_no))

if __name__ == "__main__":
    format()