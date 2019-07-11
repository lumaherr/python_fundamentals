'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width
    def __str__(self):
        return f"The area is {self.lenght * self.width} and the perimeter is {self.lenght * 2 + self.width * 2}"

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return f"The area is {self.radius * math.pi ** 2} and the circumefence is {(self.radius * 2) * math.pi}"
a = Rectangle(2, 2)
b = Circle(2)
print(a)
print(b)