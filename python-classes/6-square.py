#!/usr/bin/python3
"""
Si
"""


class Square:
    """
    Si
    """
    def validate_size(self, size):
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))
        return True

    def validate_position(self, position):
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not all(isinstance(number, int) for number in position)
                or not all(number >= 0 for number in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        return True

    def __init__(self, size=0, position=(0, 0)):
        if self.validate_position(position):
            self.__position = position
        if self.validate_size(size):
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (self.validate_size(value)):
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.validate_position(value):
            self.__position = value

    def area(self):
        return (pow(self.__size, 2))

    def my_print(self):
        if self.size == 0:
            print()
            return
        for spaces in range(self.__position[1]):
            print()
        for i in range(0, self.size):
            print(" " * self.__position[0] + "#" * self.__size)
