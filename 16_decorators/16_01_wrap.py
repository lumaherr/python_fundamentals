'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

def decorator_func(initial_func):
    def wrapper_func():
        print("The user requests the tag: ")
        return initial_func()

    return wrapper_func

@decorator_func
def paragraph_1():
    print("<p>")

@decorator_func
def header_1():
    print("<h1>")

@decorator_func
def link_1():
    print("<a>")