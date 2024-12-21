class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)

print("No, class attribute is not changed by object attribute. It is because object attribute is created and assigned to object itself. It does not change the class attribute.")