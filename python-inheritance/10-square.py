#!/usr/bin/python3
"""
Module creates a class Square
"""
Rg = __import__("9-rectangle").Rectangle


class Square(Rg):
    """
    Class will be a Square
    """
    def __init__(self, size):
        super.integer_validator("size", size)
        self.__size = size

    def area(self):
        return pow(self.__size, 2)
