#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    restrict = 'cC'

    for char in my_string:
        if char in restrict:
            continue

        new_string += char

    return new_string
