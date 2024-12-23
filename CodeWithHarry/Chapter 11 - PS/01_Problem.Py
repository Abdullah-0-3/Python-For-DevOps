class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x: {self.x}, y: {self.y}")

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")

o = TwoDVector(1, 2)
o.show()

p = ThreeDVector(1, 2, 3)
p.show()