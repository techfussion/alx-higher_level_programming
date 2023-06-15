#!/usr/bin/python3
def uniq_add(my_list=[]):
    hash_map = []
    result = 0

    for item in my_list:
        if item in hash_map:
            continue
        hash_map.append(item)
        result += item

    return result
