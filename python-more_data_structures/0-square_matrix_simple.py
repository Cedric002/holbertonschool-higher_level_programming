#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for nb1 in range(len(matrix)):
        row = []
        for nb2 in range(len(matrix[nb1])):
            row.append(matrix[nb1][nb2] ** 2)
        new_matrix.append(row)
    return new_matrix
