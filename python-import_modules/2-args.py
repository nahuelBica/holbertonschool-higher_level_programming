#!/usr/bin/python3
import sys


def print_args():
    al = sys.argv[1:]
    ac = len(al)
    msj = ("0 arguments." if ac == 0 else "1 argument:" if ac == 1 else f"{ac} arguments:")
    print(msj)
    for arg in al:
        print(f"{i}: {arg}" for i , arg in enumerate(al, start=1))

if __name__ == "__main__":
    print_args()
