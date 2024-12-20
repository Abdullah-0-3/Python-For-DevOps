# Statements

'''
break: To break out of the closest enclosing loop
continue: Go to the start of the closest enclosing loop
pass: Does nothing at all
'''

# break
for i in range(100):
    if i == 30:
        break
    print(i)

# continue
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)

# pass
for i in range(100):
    if i % 2 == 0:
        pass
    else:
        print(i)