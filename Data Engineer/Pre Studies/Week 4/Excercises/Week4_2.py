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
Rectangle with only one side length instead (since a square is equivalent to a rectangle with equal
width andheight). Reuse the Rectangle implementation for the area and perimeter calculations 
through inheriting.

Test the classes and verify that they work. 
"""
