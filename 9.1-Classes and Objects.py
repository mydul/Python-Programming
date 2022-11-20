#Class
"""Class is a variable. Lets assume a Car has different functions like Driving, Music, Fuel etc.
But Track or Boat have some extra functions so those are not same. In Python, Toyota,
Car or Track is the name of class. If we change some functions then the class will be changed."""

class Car: #We will always start the class name with an Capital-letter

"""Self is a conevntional name. We can change it too."""
"""All functions in Python class declarations must have self as their first argument, otherwise they will not work."""
    def driving(self):
        run_the_car

    def music(self):
        run_the_music

    def fuel(self):
        load_the_fuel

    def horn(self):
        make_sound_pollution

#Object
"""In our Car class have four functions. From our Car class we can made lots of transportation vehicle.
So made from a calss every vehicle is a object"""

Toyota_Car = Car()
BMW_Car = Car()
Audi_Car = Car()

#Method
"""When a function inside a class we call its a method. Only naming, else everything is the same.
Well, there is another difference. The first argument or parameter of the method will always be (self)"""

#..........Real life experinece with Class, Object, and Method or Fuctions............
print("..........Real life experinece with Class, Object, and Method or Fuctions............")

class Calculator:
    def addition(self, a, b):
        return(a+b)

    def subtraction(self, a, b):
        return a-b

    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError as e:
            print(e)
            return 'It is impossible to divide by zero.'

my_calculator = Calculator()

temp = my_calculator.addition(12, 78)
print(temp)

temp = my_calculator.subtraction(50, 23)
print(temp)

temp = my_calculator.multiplication(9, 19)
print(temp)

temp = my_calculator.division(400, 5)
print(temp)

temp = my_calculator.division(43, 0)
print(temp)