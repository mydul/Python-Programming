"""Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""

class Calculator: # The main class is (base) or (parent) class

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

class SuperCalculator(Calculator): # The new class is (child) class
    """If I inherit, the parent class must be passed in parentheses. For example, class ChildDog(ParentDog):"""

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)