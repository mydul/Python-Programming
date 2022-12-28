#..........Tuple..........
print("..........Tuple..........")

#Order immutable sequence of object in Tuple
#Write with (1st Braket)
#The difference between List and Tuple is: We cant change Tuple as our wish

a = ()
a = ("Onion", "Potato", "Ginger", 3.1416)

print(a[1:2])

# a.add("New") #'tuple' object has no attribute 'add'
a = a + ("New",)
print(a)

print(len(a))

print(a.count('Ginger'))


