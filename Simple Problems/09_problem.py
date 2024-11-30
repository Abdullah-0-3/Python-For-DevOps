# Compare two Integers

def compare(a, b):
    if a > b:
        return 'a > b'
    elif a < b:
        return 'a < b'
    else:
        return 'a == b'
    
# Test Cases
print(compare(1, 2)) # a < b
print(compare(2, 1)) # a > b
print(compare(1, 1)) # a == b