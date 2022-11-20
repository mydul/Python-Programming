#..........Basic String Operations..........
print("..........Basic String Operations..........")

astring = "Mydul Islam"
print(astring,"Lenth of String is:", len(astring)) #define lenght using len

print(astring.index("s")) #define location of s using index

print(astring.count("l")) #Count number of l using count

print(astring[6:10]) #prints a slice of the string
print(astring[6:10:3]) #The general form is [start:stop:step]
print(astring[-3]) #-3 means 3rd character from the end

print(astring[::-1]) #There is no function like strrev in C to reverse a string. But we can easily reverse a string like this

print(astring.upper()) #For uppercase 
print(astring.lower()) #For lowercase

#Check the string starts with something or ends with something
print(astring.startswith("Mydul"))
print(astring.endswith("Hossen"))

#splits the string
split = astring.split(" ")
print(split)

#...................Basic String Operations Exercise......................
print("...................Basic String Operations Exercise......................")
#My choise was : s = "Hey thera! what shou"
#Solutions will be: s = "Strings are awesome!"

s = "Hey there! what should this string be?"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))