from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you don't want that, hit RETURN.")

# take the input. If it is a return, keep on running. If it is control C, trace most recent call.
input("?")

# open the file in writing mode.
print("Opening the file...")
target = open(filename, 'w')

# Python file method truncate() truncates the file's size.
#If the optional size argument is present, the file is truncated to (at most) that size
# does not work when the file is in read-only mode
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#write can be only one string
target.write("{}\n {}\n {}\n".format(line1, line2, line3))
#writelines can use multiple strings
L=[line1, "\n", line2, "\n", line3, "\n"]
target.writelines(L)

print("And finally, we close it.")
target.close()
