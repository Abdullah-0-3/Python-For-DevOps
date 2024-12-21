class Employee():
    language = "Python"
    salary = 10000
    name = ""

    def get_info(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Hello {name}!")

harry = Employee()
harry.name = "Harry"
harry.language = "Java"
harry.get_info()
harry.greet(harry.name)