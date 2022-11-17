#! Python3
# 1.11 - Geometric Objects

# Importing necessary libraries
import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = ""

    def get_area(self):
        self.area = (self.width + self.height) * 2
        return self.area

    def __repr__(self):
        return f"Rectangle area: {self.area}"


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.area = ""

    def get_area(self):
        self.area = (self.radius**2) * math.pi
        return self.area

    def __repr__(self):
        return f"Circle area: {self.area}"


class Triangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = ""

    def get_area(self):
        self.area = (self.width * self.height) / 2
        return self.area

    def __repr__(self):
        return f"Triangle area: {self.area}"


r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)
c1 = Circle(2)
t1 = Triangle(2, 5)
t2 = Triangle(3, 1)


print(r1.get_area())

geom = [r1, r2, c1, t1, t2]
for g in geom:
    print(g.get_area())

print(geom)
