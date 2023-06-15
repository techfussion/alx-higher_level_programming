#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set()

    for item in set_2:
        if item in set_1:
            c_set.add(item)

    return c_set
