#!/usr/bin/python3

"""Prints the first x elements of a integer list"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a integer list"""
    out = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            out += 1
        except (ValueError, TypeError):
            continue
    print()
    return out
