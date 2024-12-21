# Constructor

class Employee():
    language = "Python"
    salary = 10000
    name = ""

    # Dunder Method: It is called automatically when an object is created...
    def __init__(self, name=""):
        self.name = name  # Assign name to the instance variable
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Hello {name}!")

harry = Employee("Harry")  # Pass name to the constructor
harry.language = "Java"
print(harry)
harry.greet(harry.name)