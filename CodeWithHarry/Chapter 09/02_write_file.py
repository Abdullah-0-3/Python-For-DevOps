text = 'I am doing Diploma in DevOps and Cloud Advancement.'

file = open('file.txt', 'w')
file.write(text)
file.close()

# Checking file content
file = open('file.txt', 'r')
data = file.read()
print(data)
file.close()

# Previous content will be overwritten by the w option...