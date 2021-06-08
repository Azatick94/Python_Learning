# example of simple decoration

# decorator to add lines around message
def line_decorator(func):
    def wrapper():
        print("-" * 10)
        func()
        print("-" * 10)

    return wrapper


# decorating our function with line_decorator
@line_decorator
def say_hello():
    print("Hello World!")


# running our function
say_hello()
