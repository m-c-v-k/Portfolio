#! Python3

"""
Coding Challenge 2 - Creating a class for shapes

In this challenge we are going to create a base class for shapes called 'Shape' and derive from
this to create classes for circles, rectangles and other shapes.

The base class 'Shape' should have two methods: 'area()' and 'perimeter()'. Both should return -1
in the base class - we are going to let the subclasses define these properly for themselves.
Use google to remind yourself of the different area and perimeter formulas if necessary.

Create a subclass called 'Circle' that inherits from 'Shape'. This should take in a single input in
a constructor - the radius. From this, implement the area and circumference methods for 'Circle'.

Create another subclass called 'Rectangle' that inherits from 'Shape'. This should take in the
width and height. Implement the correct versions of area and circumference for a rectangle.

Create a last subclass called 'Square' that inherits from 'Rectangle'. This should work as
Rectangle with only one side height instead (since a square is equivalent to a rectangle with equal
width andheight). Reuse the Rectangle implementation for the area and perimeter calculations
through inheriting.

Test the classes and verify that they work.
"""

# Importing necessary libraries.
import math


class Shape:
    """ Shape parent class.
    """
    def area():
        """ Empty template for calculating area.

        Returns:
            int: Template returns -1.
        """
        return -1

    def perimeter():
        """ Empty template for calculating circumference.

        Returns:
            int: Template returns -1.
        """
        return -1


class Circle(Shape):
    """ Circle class.

    Args:
        Shape (class): Parent class for shapes.
    """

    def __init__(self, radius=0):
        """ Constructor function for circles.

        Args:
            radius (int, optional): Int giving us the radius of the circle. Defaults to 0.
        """
        self.radius = radius

    def area(self):
        """ Calculates area for a circle.

        Returns:
            float: Returns the area of a circle.
        """
        self.output = math.pi * self.radius**2
        return f"Area: {self.output}"

    def perimeter(self):
        """ Calculating circumference for a circle.

        Returns:
            float: Returns the circumference of a circle.
        """
        self.output = 2 * math.pi * self.radius
        return f"Circumference: {self.output}"


class Rectangle(Shape):
    """ Rectangle class.

    Args:
        Shape (class): Parent class for shapes.
    """

    def __init__(self, width=0, height=0):
        """ Constructor function for rectangles.

        Args:
            width (int, optional): Int giving us the width of the rectangle. Defaults to 0.
            height (int, optional): Int giving us the height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    def area(self):
        """ Calculating area of a ractangle or a square.

        Returns:
            int: Returns the area of a rectangle or a square.
        """
        self.output = self.width * self.height
        return f"Area: {self.output}"

    def perimeter(self):
        """ Calculating circumference for a rectangle or a square.

        Returns:
            float: Returns the circumference of a rectangle or a square.
        """
        self.output = 2 * (self.width + self.height)
        return f"Circumference: {self.output}"


class Square(Rectangle):
    """ Square class.

    Args:
        Shape (class): Parent class for shapes.
    """

    def __init__(self, width=0):
        """ Constructor function for Squares.

        Args:
            width (int, optional): Int giving us the width of the square. Defaults to 0.
        """
        self.width = width
        self.height = width


# Functionality testing
circle = Circle(7)
print(circle.area())
print(circle.perimeter())

rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())

square = Square(5)
print(square.area())
print(square.perimeter())
