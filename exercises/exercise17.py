# EXERCISE 17 More Files
from sys import argv 
from os.path import exists

script, from_file, to_file = argv
print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")
print(f"does the output file exist? {exists(to_file)}")
print("Ready, hit Return to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")
out_file.close()
in_file.close()
