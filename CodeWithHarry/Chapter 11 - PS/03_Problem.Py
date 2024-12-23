class Employee:
    salary = 234
    increment = 20 
    
    @property
    def salaryAfterIncrement(self):
        return round((self.salary + self.salary * (self.increment/100)))

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self, salary):
        self.increment =  round(((salary/self.salary) -1)*100 )

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 300
print(e.increment)
print(e.salaryAfterIncrement)
print(e.salary)
print(e.increment)