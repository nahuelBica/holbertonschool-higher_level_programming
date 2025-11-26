#!/usr/bin/python3

"""Divide two ints"""


def safe_print_division(a, b):
    """Divide two ints"""
    out = None
    try:
        out = a / b
    except ZeroDivisionError:
        out = None
    finally:
        print("Inside result: {}".format(out))
    return out
