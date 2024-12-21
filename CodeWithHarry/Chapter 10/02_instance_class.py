class Employee():
    language = "Python"
    salary = 10000

harry = Employee()
harry.name = "Harry"
harry.language = "Java"
print(harry.name, harry.language, harry.salary)

# Instance Attribute take preference over Class Attribute