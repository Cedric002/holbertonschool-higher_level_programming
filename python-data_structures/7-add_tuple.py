def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for i in range(min(len(tuple_a), len(tuple_b))):
        result.append(tuple_a[i] + tuple_b[i])
    return tuple(result)
