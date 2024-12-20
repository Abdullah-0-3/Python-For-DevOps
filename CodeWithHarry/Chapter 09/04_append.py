text = 'I am doing Diploma in DevOps and Cloud Advancement.\n'

file = open('file.txt', 'a')
file.write(text)
file.close()

# Checking file content
file = open('file.txt', 'r')
data = file.read()
print(data)
file.close()