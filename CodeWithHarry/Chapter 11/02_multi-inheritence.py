# Multi Inheritence

class Employee:
    company = "Google"
    def show(self):
        print(f"Employee Name: {self.name}, Employee Salary: {self.salary}")

class Coder:
    language = "Python"
    def print_language(self):
        print(f"Programmer Language: {self.language}")

class Programmer(Employee, Coder):
    company = "Microsoft"
    def show_language(self):
        print(f"Programmer Company: {self.company}, Programmer Language: {self.language}")

a = Programmer()
a.print_language()
a.show_language()