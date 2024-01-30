#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_valeur = my_list[0]
        for nb in my_list[1:]:
            if nb > max_valeur:
                max_valeur = nb
        return max_valeur
