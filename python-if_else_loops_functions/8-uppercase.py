#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if c > 96 and c < 123:
            c -= 32
        print("{}".format(chr(c)), end="")
    print()
