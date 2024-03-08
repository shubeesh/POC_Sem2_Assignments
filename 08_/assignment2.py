from math import hypot, atan, degrees

class RightTrianlge:
    def _init_(self, base, height):
        self.base = base
        self.height = height
        self.angle1 = atan(self.height / self.base)
        self.angle1 = degrees(self.angle1)
        self.angle2 = atan(self.base / self.height)
        self.angle2 = degrees(self.angle2)
        self.angle1 = min(self.small_angle, self.large_angle)
        small = self.angle1
        large = self.angle2
        self.small_angle = min(small, large)
        self.large_angle = max(small, large)

    def area(self):
        
        pass

    def hypotenuse(self):
        return hypot(self.base, self.hight)
        pass

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()

triangle1 = (3, 4)
print("The area of the triangle is", triangle1.area())
print("The hypotenuse of the triangle is", triangle1.hypotenuse())
print("The perimeter of the triangle is", triangle1.perimeter())
print("The small angle of the triangle is", triangle1.small_angle)
print("The large angle of the triangle is", triangle1.large_angle)

