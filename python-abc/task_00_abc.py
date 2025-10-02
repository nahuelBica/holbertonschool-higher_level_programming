#!/usr/bin/python3
"""
Module creates a abstract class animals and two animals
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Class Animal
    """

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Subclass dog
    """

    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    subclass cat
    """

    def sound(self):
        return "Meow"
