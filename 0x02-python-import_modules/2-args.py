#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if (len == 0):
        print("{} arguments.".format(len))
    elif (len == 1):
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))
    if (len >= 1):
        idx = 0
        for arg in sys.argv:
            if (idx != 0):
                print("{}: {}".format(idx, arg))
            idx += 1
