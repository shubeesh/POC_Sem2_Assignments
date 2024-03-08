class Rectangle:
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

Rectangle1 = Rectangle
print("The base of ractangle one is", Rectangle1.base())
print("The height of rectangle one is", Rectangle1.height())
print("The area of rectangle one is", Rectangle1.area())
print("The perimeter of rectangle one is", Rectangle1.perimeter())

Rectangle2 = Rectangle
print("The base of ractangle two is", Rectangle2.base())
print("The height of rectangle two is", Rectangle2.height())
print("The area of rectangle two is", Rectangle2.area())
print("The perimeter of rectangle two is", Rectangle2.perimeter())