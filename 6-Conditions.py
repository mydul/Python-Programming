#..........Conditions..........
print("..........Conditions..........")

# Python uses boolean logic to evaluate conditions.
# The boolean values True and False are returned when an expression is compared or evaluated.
x = 1
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#Boolean operators
name = "Mydul"
age = 30
if name == "Mydul" and age == 29:
    print("Your name is Mydul, and you are 30 years old")
else:
    print("Sorry you are not in list")

#The "in" operator
name = "Mydul"
if name in ["Mydul", "Islam"]:
    print("Your name is either Mydul or islam")

#The 'is' operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#The "not" operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#...................Conditions Exercise......................
print("...................Conditions Exercise......................")
"""
Change this code

Questions:
    number = 10
    second_number = 10
    first_array = []
    second_array = [1,2,3]
"""


number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")