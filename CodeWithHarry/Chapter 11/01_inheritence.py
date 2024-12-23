class Employee:
    company = "Google"
    def show(self):
        print(f"Employee Name: {self.name}, Employee Salary: {self.salary}")

''' Instead Using Inheritance, not using this
class Programmer:
    company = "Microsoft"
    def show(self):
        print(f"Programmer Name: {self.name}, Programmer Salary: {self.salary}")

    def show_language(self):
        print(f"Programmer Language: {self.language}")
'''

class Programmer(Employee):
    company = "Microsoft"
    def show_language(self):
        print(f"Programmer Language: {self.language}")

a = Employee()
b = Programmer()

print(a.company)
print(b.company)