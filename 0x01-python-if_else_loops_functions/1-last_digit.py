#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = (repr(number)[-1])
if (int(a) > 5):
        print(f"Last digit of {number} is {a} and is greater than 5")
if (int(a) == 0):
        print(f"Last digit of {number} is {a} and is 0")
elif (int(a) < 6 != 0):
         print(f"Last digit of {number} is {a} and is less than 6 and not 0")
