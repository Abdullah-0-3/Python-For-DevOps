class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n

    def cube(self):
        return self.n * self.n * self.n

    def squareroot(self):
        return round(self.n ** 0.5, 2)

    @staticmethod
    def greet():
        print("Hello! Welcome to the best calculator of the world.")

a = Calculator(10)
print(a.greet())
print(a.square())
print(a.cube())
print(a.squareroot())