#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for char in my_list:
        if char == search:
            new_list.append(replace)
            continue
        new_list.append(char)

    return new_list
