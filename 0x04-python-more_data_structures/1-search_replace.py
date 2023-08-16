#!/usr/bin/python3
def search_replace(my_list, search, replace):
    m = my_list.copy()
    m = list(map(lambda x: replace if x == search else x, m))
    return (m)
