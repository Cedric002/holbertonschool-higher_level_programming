#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    element = 0
    nb = 0

    while nb < list_length:
        try:
            res = my_list_1[nb] / my_list_2[nb]
            result += [element]
        except ZeroDivisionError:
            print("division by 0")
            result += [0]
        except TypeError:
            print("wrong type")
            result += [0]
        except IndexError:
            print("out of range")
            result += [0]
        finally:
            nb += 1
    return result
