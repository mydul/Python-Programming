
def cal(x, y, z):

    if z == '+':
        return x + y

    if z == '-':
        return x - y

    if z == '*':
        return x * y

    if z == '/':
        return x / y

while True:
    choice = input("Enter you choice: \n")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(cal(num1, num2, choice))

    try_again = input("Press 0 to try again, any other key to exit. \n")
    if try_again != "0":
        break # break out of the outer while loop
