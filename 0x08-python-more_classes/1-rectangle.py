#!/usr/bin/python3
"""
Module creates the Rectangle class
"""


class Rectangle:
    """
    Class Rectangle with validated private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """Instantiates width and height using property setter
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: width of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: height of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the height
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = 
