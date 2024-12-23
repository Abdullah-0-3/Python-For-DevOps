# Muli Level Inheritence

class Employee:
    def __init__(self):
        print('Employee Constructor')
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print('Programmer Constructor')
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print('Manager Constructor')
    c = 3

o = Employee()
print('Employee', o.a)
# print(o.b) # (Error for B)

o = Programmer()
print('Programmer', o.a)
print('Programmer', o.b)
# print(o.c) # (Error for C)

o = Manager()
print('Manager', o.a)
print('Manager', o.b)
print('Manager', o.c)