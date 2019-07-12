'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.

- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.

- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...
'''

class Car:
    def __init__(self, model, amount, PS):
        self.model = model
        self.amount = amount
        self.PS = PS
    def __str__(self):
        return f"{self.model} is a car which is {self.amount} times in stock with {self.PS} PS"
    def Turbo(self):
        self.PS += 5
    def aging(self):
        self.PS -= 10


class Motorbike:
    def __init__(self, model, amount, PS):
        self.model = model
        self.amount = amount
        self.PS = PS
    def __str__(self):
        return f"{self.model} is a Motorbike which is {self.amount} times in stock with {self.PS} PS"

class Quad:
    def __init__(self, model, amount, PS):
        self.model = model
        self.amount = amount
        self.PS = PS
    def __str__(self):
        return f"{self.model} is a Quad which is {self.amount} times in stock with {self.PS} PS"


a = Quad("Yamaha", 5, 100)
b = Car("Porsche", 2, 300)
print(a)
print(b)
b.Turbo()
print(b)