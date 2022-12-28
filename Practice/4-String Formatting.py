#..........String Formatting..........
print("..........String Formatting..........")

name = "Islam" #tuple (a fixed size list)
country = "Bangladesh"
age = 30
print("Mydul %s is from %s. And age %d" % (name, country, age)) #two or more argument, use a tuple (parentheses)

mylist = [1,2,3,6,7]
print("A list: %s" % mylist) #repr method of that object is formatted as the string

#Note: %s - String, %d - Integers, %f - Floating numbers, %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot. %x/%X - Integers in hex representation (lowercase/uppercase)

#...................String Formatting Exercise......................
print("...................String Formatting Exercise......................")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s"
print(format_string % data)

