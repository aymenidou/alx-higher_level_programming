#!/usr/bin/python3
for i in range(0, 100):
    if (i < 99):
        print("{i:02d}".format(i), end=", ")
    else:
        print("{i:02d}".format(i))
