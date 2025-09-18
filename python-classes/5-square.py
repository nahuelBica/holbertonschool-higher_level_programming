#!/usr/bin/python3
"""
Si
"""


class Square:
    """
    Si
    """
    def validate(self, size):
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))
        return True

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (self.validate(value)):
            self.__size = value

    def __init__(self, size=0):
        if (self.validate(size)):
            self.__size = size

    def area(self):
        return (pow(self.__size, 2))

    def my_print(self):
        if self.size == 0:
            print()
            return ()
        for i in range(0, self.size):
            for y in range(0, self.size):
                print("#", end="")
            print()
