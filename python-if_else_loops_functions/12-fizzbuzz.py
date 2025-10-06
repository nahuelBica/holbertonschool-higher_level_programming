#!/usr/bin/python3

def fizzbuzz():
    for i in range(100):
        to_print = i+1
        if (i+1) % 5 == 0 and (i+1) % 3 == 0:
            to_print = "FizzBuzz"
        elif (i+1) % 5 == 0:
            to_print = "Buzz"
        elif (i+1) % 3 == 0:
            to_print = "Fizz"
        print("{}".format(to_print), end=" ")
