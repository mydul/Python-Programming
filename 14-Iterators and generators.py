#Iterators
"""List, tuple, dictionary, string objects can be iterated by for loop.
They are called iterable(Punorabritti) objects because they can be iterated. If we pass Iterable object
inside the built-in function iter(), it returns an iterator. And with the __next__() method we can access
the next element or item of an iterator. Python throws a StopIteration error
when there are no more items left to access all items."""
'''
x = iter([1, 2, 3])
x.__next__()
print(x)
'''

class Iterator:
    def __init__(self,n):
        self.n = n 
        self.i = n 

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 0:
            if self.i == self.n:
                self.n = self.n - 1
                return self.i
            else:
                self.i = self.n
                self.n = self.n - 1
                return self.i
        else:
            raise StopIteration

for temp in Iterator(10):
    print(temp)

#Generators
"""A generator also a function. The job of this function is to generate the sequence using the yield statement.
In this respect generator is also a type of iterator."""

def Generators(n):
    while n >= 0:
        yield n
        n = n - 1

for x in Generators(5):
    print(x)

# Generators form learnpython
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

#...................Generators Exercise......................
print("...................Generators Exercise......................")

# Write a generator function which returns the Fibonacci series
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break