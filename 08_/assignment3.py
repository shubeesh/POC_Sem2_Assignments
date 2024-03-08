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
        

















#class Car():
#    def __init__(self, model, colour, initial_speed=0):
#        self.model = model
#        self.colour = colour
#        if initial_speed < 0:
#            self.__speed = 0
#        else:
#            self.__speed = initial_speed

#    def speed_up(self):
#        self.__speed += 5

#    def slow_down(self):
#        if self.__speed < 5:
#            self.__speed = 0
#        else:
#            self.__speed -= 5

#    def show_speed(self):
#        print('Current speed:', self.__speed)

#my_lovely_car = Car('T-Roc', 'red', -50)
#my_lovely_car.speed = -10
#my_lovely_car.show_speed()
#print(my_lovely_car.get_model())
#my_lovely_car.__model = "chevy"
#print(my_lovely_car.__model)