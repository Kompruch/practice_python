from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(f):
    # for index, line in enumerate(f):
    #     # print(line)
    #     # a_line = f.readline()
    #     # print(a_line)
    #     print(index + 1, line)
    print(f.readline())
    

current_file = open(input_file)

# print("First let's print the whole file:\n")

# print_all(current_file)

# print("Now let's rewind, kind of like a tape.")

# rewind(current_file)

# print("Let's print three lines:")

print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)



