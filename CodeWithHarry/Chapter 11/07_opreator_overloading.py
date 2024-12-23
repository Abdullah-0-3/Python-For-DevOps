class Number:
    def __init__(self, n):
        self.n = n

    # Operator Overloading
    def __add__(self, num):
        self.n = self.n + num.n

m = Number(9)
n = Number(6)
# Error --- print(m + n)

print(m.n)