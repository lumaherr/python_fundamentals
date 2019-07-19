'''
Write a script with a function that demonstrates the use of *args.

'''

def hello_state(*germany):
    for i in germany:
        print(i)

hello_state("NRW", "Bavaria", "Berlin", "Bremen", "Hamburg")