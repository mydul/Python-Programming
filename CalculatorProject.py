import random
import math

# Take input from the user
print("Please Select the mode:")
print("1. Basic")
print("2. Scientific")
print("3. Advanced \n")
print("To Exit press 4")

choice = input("Enter you choice(1/2/3): \n")

if choice == '1':
    print("Thank you, Now you are in Basic mode-")
    print("Basic mode can perform the basic operations + × ÷ - on two input number. \n")

    while True:
        def add(x, y):
            """This function adds two numbers"""
            return x + y

        def subtract(x, y):
            """This function subtracts two numbers"""
            return x - y

        def multiply(x, y):
            """This function multiplies two numbers"""
            return x * y

        def divide(x, y):
            """This function divides two numbers"""
            return x / y

        # Take input from the user
        print("Select an operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide \n")

        choice = input("Enter choice(1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        

        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))

        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
        
        try_again = input("Press 0 to try again, any other key to exit. \n")
        if try_again != "0":
            break # break out of the outer while loop

elif choice == '2':
    print("Than you, Now you are in Scientific mode")
    print("Scientific mode can perform the basic operation and Square, Root, power, sin, cos")

    while True:
        def add(x, y):
            """This function adds two numbers"""
            return x + y

        def subtract(x, y):
            """This function subtracts two numbers"""
            return x - y

        def multiply(x, y):
            """This function multiplies two numbers"""
            return x * y

        def divide(x, y):
            """This function divides two numbers"""
            return x / y

        def square(x):
            """This function square the numbers"""
            return x

        # Take input from the user
        print("Select an operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Root")
        print("7. Power")
        print("8. Sin")
        print("9. Cos \n")

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

        num = float(input("Enter the number: "))
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1,"+",num2,"=", add(num1,num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1,"/",num2,"=", divide(num1,num2))

        elif choice == '5':
            num = float(input("Enter the number: "))
            print(num,"**",2,"=", square(num ** 2))

        elif choice == '6':
            num = float(input("Enter the number: "))
            print("√",num,"=", math.sqrt(num))
            
        elif choice == '7':
            num1 = float(input("Enter a number for value: "))
            num2 = float(input("Enter a number for power: "))
            print(num1,"**",num2,"=", pow(num1,num2))

        elif choice == '8':
            num = float(input("Enter a number: "))
            print("Sin()",num,"=", math.sin(num))

        elif choice == '9':
            num = float(input("Enter a number: "))
            print("Cos()",num,"=", math.cos(num))

        else:
            print("Invalid input")
        
        try_again = input("Press 0 to try again, any other key to exit. \n")
        if try_again != "0":
            break # break out of the outer while loop


elif choice == '3':
    print("Than you, Now you are in Advanced mode")
    print("Advanced mode with multiple basic operations on multiple input numbers")

    while True:
        def add(a, b, c, d, e):
            """This function adds two numbers"""
            return a + b +c + d + e

        def subtract(a, b, c, d, e):
            """This function subtracts two numbers"""
            return a - b - c - d - e

        def multiply(a, b, c, d, e):
            """This function multiplies two numbers"""
            return a * b * c * d * e

        def divide(a, b, c, d, e):
            """This function divides two numbers"""
            return a / b / c / d / e

        # Take input from the user
        print("Select an operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide \n")

        choice = input("Enter choice(1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num = float(input("Enter the number: "))

        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))

        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
        
        try_again = input("Press 0 to try again, any other key to exit. \n")
        if try_again != "0":
            break # break out of the outer while loop

elif choice == '4':
    print("Oh! you selected to exit") 
    exit()
    # we can use sys.exit or exit() or quit() functions also

else:
    print("Invalid input")



