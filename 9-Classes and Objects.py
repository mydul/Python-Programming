#..........Classes and Objects..........
print("..........Classes and Objects..........")

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message from inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

myobjectx.function()
myobjecty.function()

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

#New CLass
class NumberHolder:

   def __init__(self, number):
       self.number = number #To access an attribute variable within a Python class, self. should be prefixed with,
       #Like self.attributeName

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

#..........Classes and Objects Exercise..........
print("..........Classes and Objects Exercise..........")
'''
We have a class defined for vehicles. Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be
a blue van named Jump worth $10,000.00.
'''
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
    car1 = Vehicle()
    car1.name = "Fer"
    car1.color = "red"
    car1.kind = "convertible"
    car1.value = 60000.00

    car2 = Vehicle()
    car2.name = "Jump"
    car2.color = "blue"
    car2.kind = "van"
    car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())