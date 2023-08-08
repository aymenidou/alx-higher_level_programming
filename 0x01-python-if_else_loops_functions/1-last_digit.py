#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
static = number
if (number < 0):
    number *= -1
last_digit = number % 10
str1 = "Last digit of {static} is {last_digit} "
if (last_digit > 5):
    str1 += "and is greater than 5"
elif (last_digit == 0):
    str1 += "and is 0"
elif (last_digit < 6):
    str1 += "and is less than 6 and not 0"
print(f"{str1}".format(static=static, last_digit=last_digit))
