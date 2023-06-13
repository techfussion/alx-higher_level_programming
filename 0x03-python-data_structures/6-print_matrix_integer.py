#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for item in sublist:
            print('{}'.format(item), end=' ')

        print('')
