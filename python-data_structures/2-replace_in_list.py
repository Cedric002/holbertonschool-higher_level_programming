#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        return my_list
