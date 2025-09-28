#!/usr/bin/python3
"""
Function used to check if an object is a subclass of a class
"""


def inherits_from(obj, a_class):
    """
    Function used to check if an object is a subclass of a class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
