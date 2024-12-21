# Object Oriented Programming

'''
Object Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation. Today, many popular programming languages (such as Java, JavaScript, C#, C++, Python, PHP, Ruby and Objective-C) support OOP.
'''

class Employee:
    language = "Python" # Class Attribute
    salary = 10000

harry = Employee()
harry.name = "Harry" # Object Attribute (Instance Attribute)
print(harry.name, harry.language, harry.salary)

larry = Employee()
larry.name = "Larry"
print(larry.name, larry.language, larry.salary)