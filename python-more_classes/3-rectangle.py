#!/usr/bin/python3
"""
Module creates a class rectangle
"""


class Rectangle:
    """
    Class will be a rectangle
    """

    def validate_size(self, value, axis):
        if type(value) is not int:
            raise (TypeError(f"{axis} must be an integer"))
        if value < 0:
            raise (ValueError(f"{axis} must be >= 0"))
        return True

    def __init__(self, width=0, height=0):
        if self.validate_size(width, "width"):
            self.__width = width
        if self.validate_size(height, "height"):
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (self.validate_size(value, "width")):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.validate_size(value, "height"):
            self.__height = value

    def __str__(self):
        if ((self.__width or self.__height) == 0):
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))
