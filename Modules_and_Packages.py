#..........Modules and Packages 1..........
print("..........Modules and Packages 1..........")

#11.1-Modules_and_Packages.py
def fib(n):
    series = []
    a, b = 0, 1
    while b < n:
        series.append(b)
        a, b = b, a+b
    return series

if __name__ == "__main__":
    temp = fib(100)
    print(temp)



#..........Modules and Packages Exercise 1..........
print("..........Modules and Packages Exercise 1..........")