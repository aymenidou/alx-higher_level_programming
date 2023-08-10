#!/usr/bin/python3
for i in range(26, 0, -1):
    if (i % 2 == 0):
        print("{:s}".format(chr(96 + i)), end="")
    else:
        print("{:s}".format(chr(64 + i)), end="")
