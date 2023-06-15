#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sub_list in matrix:
        squared_list = []
        for item in sub_list:
            squared_list.append(item ** 2)

        new_matrix.append(squared_list)

    return new_matrix
