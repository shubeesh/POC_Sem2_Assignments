def get_area(self) -> float:
    return self.__base * self.__height


def __str__(self) -> str:
    rectangle1 = rectangle(3,4)
    return "rectangle with base" + str(self.__base) + ", height" + str(self.height)

class rectangle:
    def __init__(self, height, float):
        self.height = height

class square(rectangle):
    def __init__(self, height, float):
        super().__init__(height)
        self.float = float
        print(super().class_message)


square1 = square(3, 3)
print(square1)
print("The base of the square is", square1.get_base())
print("The height of the square is", square1.get_height())
print("The area of the square is", square1.float())

