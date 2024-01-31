#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nbs = {}
    for nb in my_list:
        if nb not in unique_nbs:
            unique_nbs[nb] = 1
    return sum(unique_nbs.values())
