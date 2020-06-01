# Functions and Files
from sys import argv

script, input_file = argv
# define a function alled print_all which reads the entire file and print it out.
def print_all(f):
    print(f.read())
#define a function called rewind which the file position to position 0.
# Seek changes the file position to the indicated byte in the file.
def rewind(f):
    f.seek(0)
# Readline return list of lines in the file, with optional size argument
def print_a_line(line_count,f):
    print(line_count,f.readline())
# open input file from argv
current_file = open(input_file)

print("First let's print the whole file: \n")
# Use the print_all function to read the file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# Use rewind function to get back to position 0
rewind(current_file)

print("Let's print three lines:")
# read the first line
current_line = 1
print_a_line(current_line, current_file)
# read the next line
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# read the next line.
current_line += 1
#current_line = current_line + 1
print_a_line(current_line, current_file)
