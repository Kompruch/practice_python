def print_two(*args):
    for word in args:
        print(word)


print_two("AAA","BBB","CCC","DDD")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two_again("Zed","Shaw")

def print_none():
    print("I got nothin'.")

print_none()