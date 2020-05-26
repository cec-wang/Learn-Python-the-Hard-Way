#imporr argv library
from sys import argv

#input file name. script is the python file name.
script, filename = argv

# open the file
txt = open(filename)

#read the file
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
txt.close()
