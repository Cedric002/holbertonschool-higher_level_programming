#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()

    max_len = max(len(tuple_a), len(tuple_b))

    for nb in range(max_len):
        result += ((tuple_a[i] if nb < len(tuple_a) else 0) +
                   (tuple_b[i] if nb < len(tuple_b) else 0),)

    return result
