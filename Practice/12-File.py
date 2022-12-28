#..........file..........
print("..........file..........")
"""In file we can (open), then (read), then (write) and (close)
But for that with this script have to create a file in the same directory.

Mode:
Read Only ('r') : Open text file for reading.
Read and Write ('r+'): Open the file for reading and writing.
('rb'): Like 'r' but open in Binary formate.
('rb+'): Combination of 'r+' and 'rb'

Write Only ('w') : Open the file for writing.
Write and Read ('w+') : Open the file for reading and writing.
('wb'): Like 'w' but open in Binary formate.
('wb+'): Combination of 'w+' and 'wb'

Append Only ('a'): Open the file for writing.
Append and Read ('a+') : Open the file for reading and writing.
('ab'): Like 'a' but open in Binary formate.
('ab+'): Combination of 'a+' and 'ab'"""

my_file = open('file.txt', 'r')
content = my_file.read()
print(content)
my_file.close()

my_file = open('file.txt', 'w')
my_file.write('I am Mydul Islam.')
print(content)
my_file.close()

my_file = open('file.txt', 'a')
my_file.write('I am from Bangladesh.')
print(content)
my_file.close()

