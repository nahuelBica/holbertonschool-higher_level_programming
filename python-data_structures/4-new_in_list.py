#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    cl = my_list.copy()
    if idx < 0:
        return cl
    if idx >= len(my_list):
        return cl
    cl[idx] = element
    return cl
