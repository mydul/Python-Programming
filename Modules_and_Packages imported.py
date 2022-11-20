import Modules_and_Packages
series = Modules_and_Packages.fib(100)
for item in series:
    print(item)

#or

from Modules_and_Packages import fib
series = fib(100)
for item in series:
    print(item)

#We can import all attribute from a module by using "from ... import *"
from Modules_and_Packages import *
series = fib(150)
for item in series:
    print(item)
