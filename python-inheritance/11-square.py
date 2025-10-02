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
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(super().__width, super().__height)
