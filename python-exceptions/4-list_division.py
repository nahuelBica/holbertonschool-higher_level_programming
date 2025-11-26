#!/usr/bin/python3

"""Divide elements of 2 list"""


def list_division(my_list_1, my_list_2, list_length):
    """Divide elements of 2 list"""
    out = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            out.append(ans)
    return out
