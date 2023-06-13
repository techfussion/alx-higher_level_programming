#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for item in sublist:
            print('{:d}'.format(item), end=' ' if item != sublist[-1] else '')

        print('')
