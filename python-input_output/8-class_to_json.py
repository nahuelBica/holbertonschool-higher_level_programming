#!/usr/bin/python3
"""
Generate json from object in a class
"""


def class_to_json(obj):
    return obj.__dict__
