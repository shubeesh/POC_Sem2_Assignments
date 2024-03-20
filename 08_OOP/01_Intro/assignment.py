class RightTriangle:
    def __init__(self, base, height):
        self.base = base

    def __init__(self, base, height):
        self.height = height
    
    def area(self):
        return 1/2 * self.base * self.height

triangle1 = RightTriangle(3, 4)
triangle2 = RightTriangle(5, 7)
print("The area of triangle1 is", triangle1.area())
print("The area of triangle2 is", triangle2.area())
print(triangle2.area())