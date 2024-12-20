line_no = 1

with open("logs.txt", "r") as f:
    line = f.readline()

for line_no in line:
    if 'python' in line.lower():
        print("Python is present in line number", line_no)
        break
    line_no += 1
else:
    print("No, Python is not present")