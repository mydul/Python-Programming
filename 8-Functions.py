#..........Functions..........
print("..........Functions..........")
'''Ruti making machine is the Function.
To making ruti in machine: water & flour are two Parameter.
Where Ruti is the return. Function can't return more then One.
2 types of function: 1. built-in (print(), input(), pop()) 2. user-defined

Functions in python are defined using the block keyword "def",
followed with the function's name as the block's name.'''

def print_my_name(myname):
    # This will print the given name
    print('The given name is', myname)
    return
print_my_name('Mydul')

#A variable can be declaired intead of Parameter. Like-
def print_my_name(myname):
    # This will print the given name
    print('The given name is', myname)
    return

name = "Mydul"
print_my_name(name)



#Functions may also receive arguments (variables passed from the caller to the function)
def my_function_with_greeting(username, greeting): 
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum(a, b):
    return a + b #Functions may return a value to the caller, using the keyword- 'return'
my_function_with_greeting("John Doe", "Have a nice day")


#..........Functions Exercise..........
print("..........Functions Exercise..........")

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
    "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
