# Question 5

words = ['copun', 'click', 'subscribe']

with open("censord.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))
    with open("censord.txt", "w") as f:
        f.write(content)