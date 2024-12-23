class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __mul__(self, c):
        mulReal = self.real * c.real - self.imag * c.imag
        mulImag = self.real * c.imag + self.imag * c.real
        return Complex(mulReal, mulImag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
print(c1 * c2)