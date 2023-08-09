#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
original = number
if (number < 0):
    number *= -1
last_digit = number % 10
str1 = "Last digit of {original} is "
if (last_digit > 5 and original > 0):
    str1 += "{last_digit} and is greater than 5"
elif (last_digit == 0 and original > 0):
    str1 += "{last_digit} and is 0"
elif (last_digit < 6):
    if (original < 0):
        str1 += "-"
    str1 += "{last_digit} and is less than 6 and not 0"
print(f"{str1}".format(original=original, last_digit=last_digit))
