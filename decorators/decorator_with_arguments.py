def do_twice(func):
    def inner_function(*args):
        func(*args)
        func(*args)

    return inner_function


@do_twice
def print_message(name):
    print("Hello World "+name+"!")


# calling decorated message with Argument
print_message("Azat")