#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while (True):
            print("{}".format(my_list[i]), end="")
            i += 1
            if (x == i):
                print("")
                break
    except:
        print("")
    return (i)
