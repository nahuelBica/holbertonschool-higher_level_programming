#!/usr/bin/python3

"""function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):

    """function that prints x elements of a list."""

    out = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            out += 1
    except IndexError:
        pass
    print()
    return out
