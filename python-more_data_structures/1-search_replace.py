#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for element in range(len(my_list) - 1):
        if my_list[element] == 89:
            my_list[element] = 2
    return my_list
