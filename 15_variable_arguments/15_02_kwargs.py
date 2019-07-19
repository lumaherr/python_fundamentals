'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def cars(**PS):
    for a,b in PS.items():
        print(a,b)

cars(Porsche = "500", Maserati = "600", Audi = "200")