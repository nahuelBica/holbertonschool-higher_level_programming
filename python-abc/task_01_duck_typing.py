#!/usr/bin/python3
"""
Module creates a abstract class shape and two shapes
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Class Shape
    """

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    """
    Subclass Circle
    """
    def __init__(self, radius):
        if (radius is not float or radius < 0):
            raise Exception ("El radio debe ser un número positivo")
        self.__radius = radius

    def area(self):
        return ((2 * 3.14) * self.__radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return abs((self.__width + self.__height) * 2)


def shape_info(any_shape):
    print(f"Area: {any_shape.area()}")
    print(f"Perimeter: {any_shape.perimeter()}")
