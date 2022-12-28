#..........Basic Operators..........
print("..........Basic Operators..........")

#Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

modulo = 26 % 5
print(modulo)

squred = 5 ** 2
cubed = 3 ** 3
print(squred,"and", cubed)

#Using Operators with Strings
Loveu = "LoveYou" * 10
print(Loveu)

#Using Operators with Lists
even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#multiplication operator
print([5,7,8] * 3)

#...................Basic Operators Exercise......................
print("...................Basic Operators Exercise......................")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

