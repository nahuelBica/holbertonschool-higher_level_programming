#!/usr/bin/python3
"""
Module creates a class Rectangle
"""
Bg = __import__("7-base_geometry").BaseGeometry


class Rectangle(Bg):
    """
    Class will be a Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        