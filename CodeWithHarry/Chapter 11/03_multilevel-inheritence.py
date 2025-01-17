# Muli Level Inheritence

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
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