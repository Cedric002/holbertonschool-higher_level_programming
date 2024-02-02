#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if not (isinstance(my_list_1[i], int) or
                    isinstance(my_list_1[i], float)):
                raise TypeError("wrong type")
            if not (isinstance(my_list_2[i], int) or
                    isinstance(my_list_2[i], float)):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result.append(my_list_1[i] / my_list_2[i])
        except Exception as e:
            print(e)
            result.append(0)
    return result

