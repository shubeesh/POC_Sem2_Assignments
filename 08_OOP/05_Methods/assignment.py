class __Rectangle:
    def _init_(self, base, height) -> None:
        self.__base = base
        self.__height = height

    def get_height(self) -> float:
        return self.__height

    def get_base(self) -> float:
        return self.__base

    def get_perimeter(self)-> float:
        return 2 * self.__base + 2 * self.__height

    def get_area(self) -> float:
        return self.__base * self.height

    def get_count(self) -> float:
        return self.get_count

    def __str__(self):
        return "Rectangle of base" + self.__base + ", height", + self.__height 

Rectangle1 = __Rectangle(5, 3)
print("The base of ractangle one is", Rectangle1.get_base())
print("The height of rectangle one is", Rectangle1.get_height())
print("The area of rectangle one is", Rectangle1.get_area())
print("The perimeter of rectangle one is", Rectangle1.get_perimeter())
print("")
Rectangle2 = __Rectangle(6, 8)
print("The base of ractangle two is", Rectangle2.get_base())
print("The height of rectangle two is", Rectangle2.get_height())
print("The area of rectangle two is", Rectangle2.get_area())
print("The perimeter of rectangle two is", Rectangle2.get_perimeter())
print(__Rectangle.get_count())
print("")