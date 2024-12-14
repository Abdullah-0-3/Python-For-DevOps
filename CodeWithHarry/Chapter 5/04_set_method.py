# Sets Methods

s = {1, 3, 5, 7, 9}

# add() method
s.add(4)
print('Add Method', s)

# remove() method
s.remove(3) 
print('Remove Method',s)

# discard() method
s.discard(5)
print('Discard Method', s)

# pop() method
s.pop()
print('Pop Method:', s)

# clear() method
s.clear()
print('Clear Method', s)

# del keyword
del s
try:
    print(s)
except NameError:
    print('NameError: s is not defined')