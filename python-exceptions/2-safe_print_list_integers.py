#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for integer in range(x):
            if isinstance(my_list[integer], int):
                print("{:d}".format(my_list[integer]), end=' ')
                count += 1
    except IndexError:
        pass
    print()
    return count
