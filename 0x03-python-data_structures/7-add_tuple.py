#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []

    for i in range(2):
        try:
            item_1 = tuple_a[i]
        except IndexError:
            item_1 = 0

        try:
            item_2 = tuple_b[i]
        except IndexError:
            item_2 = 0

        result.append(item_1 + item_2)

    return tuple(result)
