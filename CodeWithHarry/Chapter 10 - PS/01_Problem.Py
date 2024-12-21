# Question 01

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, postal_code):
        self.name = name
        self.salary = salary
        self.postal_code = postal_code

    def getDetails(self):
        return f"The name of the employee is {self.name}, salary is {self.salary}, postal code is {self.postal_code} and works at {self.company}."

p = Programmer("Shivam", 100000, 44100)
q = Programmer("Harry", 120000, 44100)
r = Programmer("Rohan", 130000, 44100)
s = Programmer("Abdullah", 140000, 44100)

print(p.getDetails())
print(q.getDetails())
print(r.getDetails())
print(s.getDetails())