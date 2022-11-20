#..........Dictionaries..........
print("..........Dictionaries..........")
"""
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
Each value stored in a dictionary can be accessed using a key, which is any type of object (a string,
a number, a list, etc.) instead of using its index to address it.
"""
phonebook = {}
phonebook["Polash"] = 491938477566
phonebook["Mehrab"] = 491938377264
phonebook["Amran"] = 491947662781
print(phonebook)

#At different notation

phonebook = {
    "Polash" : 491938477566,
    "Mehrab" : 491938377264,
    "Amran" : 491947662781
}
del phonebook["Mehrab"] #Removing a value
phonebook.pop("Polash") #Removing a value (another way)
print(phonebook)

phonebook = {"Polash" : 491938477566,"Mehrab" : 491938377264,"Amran" : 491947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


#..........Dictionaries Exercise..........
print("..........Dictionaries Exercise..........")

#Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")