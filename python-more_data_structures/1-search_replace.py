#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for element in range(len(my_list)):
        if my_list[element] == search:
            my_list[element] = replace
    return my_list
