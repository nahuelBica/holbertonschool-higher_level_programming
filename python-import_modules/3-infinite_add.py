#!/usr/bin/python3
"""Ex 3"""


if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    sum = 0

    for arg in argv:
        sum += int(arg)

    print(sum)
