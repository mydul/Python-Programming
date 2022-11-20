#..........Set..........
from typing import Set


print("..........Set..........")

#Set is a Data tipe like list
#Write with {2nd Braket}
#The difference between List and Set is: One item can be include in set 1 times

set = {}
set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} #One item can be print in set 1 times in Set

print(set)
print(len(set))

set.add("Pineapple")
print(set)

# Interesting thing is Set prints value in different orders everytime

set.update("Berry", "Grape") #We did a mistek here, We have to add items within {} inside a ()
print(set)
print(len(set))

# set.remove("Berry") #remove can remove one item once but if the item dosent mach it show error
set.discard("Grape") #discard function dont dosent show any error even not mach. Its safe.

set.update({"Berry", "Grape"})
print(set)

# Normally we can't creat empty set in python like myset ={}. It will be a Dictionary. So for making empty set, have to write-
myset = set() #Carefully not Set(), only set()

a = {5, 7, 2}
b = {1, 2, 3, 6}

# Union (Two set together)
print(a.union(b))

# intersection
print(a.intersection(b))

# difference
print(a.difference(b))
print(b.difference(a))
