#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None

    current_max = 0

    for num in my_list:
        if num > current_max:
            current_max = num

    return current_max
