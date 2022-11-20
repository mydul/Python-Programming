"""While studying about class we have seen some methods like __init__(), __iter__(), __next__().
Apart from these three, Python has many more special methods surrounded by double underscores.
They are called magic method. Because they bring magic to class activities.
If there are two underscores before and after, it is called dunder.And while reading it is read as 'dunder init'."""

#Comparison Magic Method
""" __cmp__(self, other) is the parent of all comparison operators
    __eq__(self, other) == operator works
    __ne__(self, other) works with the != operator
    __lt__(self, other) does the < operator
    __gt__(self, other) > operator works
    __le__(self, other) <= operator works
    __ge__(self, other) >= operator works
"""

#Arithmetic Magic Method
""" __add__(self, other) + operator
    __sub__(self, other) - operator
    __mul__(self, other) * operator
    __div__(self, other) / operator
    __mod__(self, other) % operator
    __pow__             ** operator
    __floordiv__(self, other) // operator
"""

#Type conversion magic method
""" __int__(self) converts to an integer
    __float__(self) converts to a float
    __str__(self) converts to a human-readable string
    __repr__(self) converts to a machine-readable string
"""

#Some other magic methods
""" __len__(self) Returns the length of the container
    __iter__(self) Returns the iterator for the container
    __contains__(self, item) Tests whether item is a member of a container

"""
class MyClass:
    """A custom class"""

    def __init__(self, var): # __init__(self, [...]) Constructs the class
        self.var = var

    def __del__(self): # __del__(self) Destructs the class
        del self.var

    def __gt__(self, other):
        return len(other) > len(self.var)

    def __lt__(self, other):
        return len(other) < len(self.var)

    def __ge__(self, other):
        return len(other) >= len(self.var)

    def __le__(self, other):
        return len(other) <= len(self.var)
    
a = 'Bangladesh'
b = 'desh'
a.__len__()
a.__iter__()
list(a.__iter__())
['B', 'a', 'n', 'g', 'l', 'a', 'd', 'e', 's', 'h']
a.__contains__(b)