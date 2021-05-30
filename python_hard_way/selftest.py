from sys import argv
from os.path import exists

script, from_file, to_file = argv

with open(from_file) as in_file:
    data = in_file.read()

print("If file exists {}".format(exists(to_file)))

with open(to_file, mode="w") as out_file:
    out_file.write(data)

print("All DONE!")


