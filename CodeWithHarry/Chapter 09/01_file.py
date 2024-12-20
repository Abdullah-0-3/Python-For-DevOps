# File I/O

'''
File Types:
    1. Text Files
    2. Binary Files

File Modes:
    1. Read Mode (r)
    2. Write Mode (w)
    3. Append Mode (a)
    4. Read and Write Mode (r+)
    5. Write and Read Mode (w+)
    6. Append and Read Mode (a+)
'''

file = open('file.txt', 'r')
data = file.read()
print(data)
file.close()