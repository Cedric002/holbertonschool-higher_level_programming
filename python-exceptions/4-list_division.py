#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if my_list_1 is not None or my_list_2 is not None:

        for nb in range(0, list_length):
            result = 0
            try:
                result = my_list_1[nb] / my_list_2[nb]
            except ZeroDivisionError:
                print('division by 0')
            except IndexError:
                print('out of range')
            except TypeError:
                print('wrong type')
            finally:
                new_list.append(result)
        return new_list
