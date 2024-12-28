# Format Function in Python

name = "{} is a {} programmer".format("John", "Python")
print(name)

name = "{1} is a {0} programmer".format("Python", "John")
print(name)

name = "{name} is a {language} programmer".format(name="John", language="Python")
print(name)

name = "{0} is a {language} programmer".format("John", language="Python")
print(name)

name = "{0} is a {1} programmer".format("John", "Python")
print(name)

name = "{0} is a {1} programmer and {0} is also a {1} programmer".format("John", "Python")
print(name)