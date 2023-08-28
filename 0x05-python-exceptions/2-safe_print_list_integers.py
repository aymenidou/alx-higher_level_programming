#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0

    while (True):
        try:
            if (x <= i):
                break
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            i += 1
        except TypeError:
            i += 1
        else:
            i += 1
            printed += 1
    print()
    return (printed)
