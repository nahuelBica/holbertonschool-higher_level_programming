#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = new_element
    return new_list
