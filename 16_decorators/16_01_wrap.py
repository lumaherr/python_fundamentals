'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

def decorator_func(initial_func):
    def wrapper_func(*args, **kwargs):
        print("The user requests the tag: ")
        return initial_func(*args)

    return wrapper_func

@decorator_func
def paragraph_1(abc):
    print(f"<p> {abc} </p>")

@decorator_func
def header_1(abc):
    print(f"<h1> {abc} <h1>")

@decorator_func
def link_1(abc):
    print(f"<a> {abc} <a>")

input1 = input("Please type something: ")
paragraph_1(input1)
header_1(input1)
link_1(input1)
