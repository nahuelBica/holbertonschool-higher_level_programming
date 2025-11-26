#!/usr/bin/python3

"""print the value as an integer or except"""


def safe_print_integer(value):
    """print the value as an integer or except"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
