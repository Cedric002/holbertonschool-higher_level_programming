#!/usr/bin/python3
def delete_at(my_list=[], idex=0):
    if idex < 0 or idex >= len(my_list):
        return my_list
    del my_list[idex]
    return my_list
