#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for i in range(len(my_string)):
        if (my_string[i] not in "Cc"):
            result += my_string[i]
    return result
