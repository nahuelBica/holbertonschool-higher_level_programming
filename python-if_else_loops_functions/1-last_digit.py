#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 if number >= 0 else -number % 10
strbase = "Last digit of " + str(number) + " is " + str(digit)
if (digit > 5):
    print(f'{strbase} and is greater than 5')
elif (digit == 0):
    print(f'{strbase} and is 0')
else:
    print(f'{strbase} and is less than 6 and not 0')
