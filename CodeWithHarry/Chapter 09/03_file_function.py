f = open("text.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

# Reading Each Line

f = open("text.txt")

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
line5 = f.readline()
line6 = f.readline()
line7 = f.readline()
f.close()

print('--', line1)
print('--', line2)
print('--', line3)
print('--', line4)
print('--', line5)
print('--', line6)
print('--', line7)

# Using Loop

f = open("text.txt")

line = f.readline()
while line != '':
    print(line)
    line = f.readline()

f.close()