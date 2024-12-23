# Class Method

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print('Employee Class Method', cls.a)

e = Employee()
e.a = 10
e.show()