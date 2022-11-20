#..........Errors & Exceptions..........
print("..........Errors & Exceptions..........")

"""#Exception is an event that occurs when a problem occurs while the program is running

FileNotFoundError: is raised when a specified file cannot be found to exist.
ImportError: is raised when an import statement fails.
IndentationError: Raised when indentation is not properly maintained in a codeblock.
IndexError: is raised when a specified index cannot be found in a sequence.
KeyboardInterrupt: is raised when the user interrupts the execution of a program by pressing Ctrl + C.
KeyError: is raised when a specified key cannot be found in the dictionary.
NameError: is raised when the specified local or global variable cannot be found.
OSError: Raised when a system function returns a system-related error.
RuntimeError: Raised when no general standard exception is available to handle an error.
StopIteration: is raised when the next() method no longer points to an object.
SyntaxError: is raised when there is a syntax error.
SystemError: Raised when the Python interpreter detects an internal error.
TabError: is raised when code is indented with tabs and spaces at the same time.
TypeError: is raised when a function or operation is applied to an object of an incompatible type.
UnboundLocalError: This is a descendant of NameError. Raise occurs when a local variable is used in a function or method but the variable has no value.
ValueError: is raised when a built-in operation or function accepts an argument whose type is correct but the value is messed up and the problem cannot be masked with IndexError.
WindowsError: is raised when there is a problem with the Windows operating system.
ZeroDivisionError: Raised when an attempt is made to divide a value by zero. """

#Example 1
print("\n..........Example 1..........")
try: #Where problem occurs
    my_file = open('test.txt', 'r')
    content = my_file.read()
    print(content)
    my_file.close()

except FileNotFoundError as e: #Handeling error
    print(e) #Use e for Exceptions throing message to print
    print("\n Actually, The file does not exist. That's why 'FileNotFoundError' problem occurs.")
    print("'Made by Mydul'")


#Example 2
print("\n..........Example 2..........")
try: #There are no problem in this code
    a = 5
    b = 8
    print(a+b)

except ValueError as e:
    print(e)
else: #So else block executed and printed
    print('There is no exception.')
finally: #The finally(clean-up action) block sits at the very end.
    print("And whether or not an exception is raised")


#Example 3
print("\n..........Example 3..........")
try:
    raise NameError('Hey! It is a custom error message. We can raise them ourselves if we want.')
except NameError as e:
    print(e)
    