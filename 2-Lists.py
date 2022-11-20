#..........Lists..........
print("..........Lists..........")

newlist = []
newlist.append(5)
newlist.append(6)
newlist.append(7)
print(newlist[0])
print(newlist[1])
print(newlist[2])

# prints out 1,2,3 together
for x in newlist:
  print(x)

mylist = [1,2,3]
print(mylist[2])

# Sum all the elements of a list
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

#...................Lists Exercise......................
print("...................Lists Exercise......................")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)