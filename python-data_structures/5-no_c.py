#!/usr/bin/python3
def no_c(my_string):
    out = ''
    for i in my_string:
        if i == 'C' or i == 'c':
            continue
        else:
            out += i
    return out
