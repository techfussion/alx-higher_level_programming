#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set()

    for item in set_1:
        od_set.add(item)

    for item in set_2:
        od_set.add(item)

    return od_set
