#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list
    if (idx < 0 or idx >= len(my_list)):
        return "None"
    else:
        cp_list[idx] = element
        return cp_list
