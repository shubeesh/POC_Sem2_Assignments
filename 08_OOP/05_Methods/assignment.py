<<<<<<< HEAD
class __Rectangle:
    def _init_(self, base, height) -> None:
        self.__base = base
        self.__height = height
=======
class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height
>>>>>>> 5c030099a6f7f0d41ea1561df69d4895f3aee891

    def get_height(self) -> float:
        return self.__height

<<<<<<< HEAD
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
=======
    # YOUDO the get_base method

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    # Youdo get_area method
    
    def __str__(self) -> str:
        # Rectangle of base:3, height:4
        return "Rectangle of base:" + self.__base + ", height:" + self.__height
        pass


# YOUDO>  create two rectangles.  print their base, height, perimeter, and area
# using only the methods not the fields/property/attributes
>>>>>>> 5c030099a6f7f0d41ea1561df69d4895f3aee891
