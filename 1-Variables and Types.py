#..........Variables and Types..........
print("..........Variables and Types..........")

# To define a Integer or floating number
int = 5.3
print(int)
int = float(5)
print(int)

# Normal calculation
x = -3
y = 4
sum = x + y
print(sum)

# Strings are defined either with a single quote or a double quotes
mystring1 = 'Hello'
print(mystring1)
mystring2 = "World"
print(mystring1)
hw = mystring1 + " " + mystring2
print(hw)

# But using double quotes makes it easy to include apostrophes
string = "Please Don't make a noise"
print(string)

# Assignments can be done on more than one variable on the same line
a, b, c = 7, 9, 86
print(a + b + c)
d, e, f = 100, "bar", "bolechi"
print(d, e, f)

#...................Variables and Types Exercise......................
print("...................Variables and Types Exercise......................")
"""
mystring = None
myfloat = None
myint = None
"""
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)



