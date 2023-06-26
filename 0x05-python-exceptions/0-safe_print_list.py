#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    try:
        for item in my_list:
            if nb_print == x:
                return nb_print

            print(item, end='')
        print()
    except IndexError:
        pass

    return (nb_print)
