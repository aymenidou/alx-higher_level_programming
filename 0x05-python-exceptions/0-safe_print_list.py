#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    try:
        while (True):
            print("{:d}".format(my_list[i]), end="")
            i += 1
            if (x == i):
                print("")
                break
    except Exception:
        print("")
    return (i)
