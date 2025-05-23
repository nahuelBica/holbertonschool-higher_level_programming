#!/usr/bin/python3
import sys


def print_args():
    al = sys.argv[1:]
    ac = len(al)
    msj = ("0 arguments." if ac == 0 else "1 argument:" if ac == 1 else f"{ac} arguments:")
    print(msj)
    for i,arg in enumerate(al, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_args()
