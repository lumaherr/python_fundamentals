'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

class Supercar(Car):
    def supercar1(self):
        print("this car is very fast")

class oldtimer(Car):
    def old(self):
        print("this car is very old")

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
c = oldtimer("Porsche", 2, 300)
d = Supercar("Porsche", 2, 300)
print(a)
print(b)
b.Turbo()
print(b)
c.old()
d.supercar1()