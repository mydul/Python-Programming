#..........Lambda functions..........
print("..........Lambda functions..........")

#Normally
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

""" Now instead of defining the function somewhere and calling it, we can use python's lambda functions,
    which are inline functions defined at the same place we use it.
    So we don't need to declare a function somewhere and revisit the code just for a single time use.
    Don't need to have a name, so they also called anonymous functions. We define a lambda function using the keyword lambda."""
# Like: my_function_name = lambda inputs : output

#So the above sum example using lambda function would be,
a, b = 1, 2
sum = lambda x,y : x + y
print(sum(a,b))

#..........Lambda functions Exercise..........
print("..........Lambda functions Exercise..........")

""" Write a program using lambda functions to check if a number in the given list is odd.
    Print "True" if the number is odd or "False" if not for each element."""

l = [2,4,7,3,14,19]
for i in l:
    test_lambda = lambda x : (x % 2) == 1
    print(test_lambda(i))

#Lambda function to find the smaller value between two
a, b = 5, 8
get_min = lambda a, b : a if a < b else b
print(get_min(a, b))

#or using min() function

a, b, c = 5, 8, 2
get_min = lambda a, b, c : min(a,b,c)
print(get_min(a, b, c))

#Using Function
"""def g(list, f):
    min = list[0]
    for i in list:
        if f(i) < f(max):
             min = i
    return min
"""
# Find lowest number in array by lambda function!!

l = [2,4,7,3,14,19]
for i in l:
    min_lambda = lambda i, l : min(i, l)
    print(min_lambda(i))