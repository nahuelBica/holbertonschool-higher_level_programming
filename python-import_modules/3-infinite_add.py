#!/usr/bin/python3
import sys
from calculator_1 import add


def inf_sum():
    al = sys.argv[1:]
    sum = 0
    for i in range(len(al)):
        sum = add(sum, int(al[i]))
    print(sum)


if __name__ == "__main__":
    inf_sum()
