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
