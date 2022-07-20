# EXERCISE 16 Reading and Writing Files

from sys import argv
script, filename = argv

print(f"we are going to erase {filename}.")
print("if you dont want that, hit CTRL-c (^C).")
print("if you want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("truncating the file. GoodBye!")
target.truncate()
print("Now i am going to ask for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()
