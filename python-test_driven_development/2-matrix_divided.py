#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    The list of the matrix must be a integers or floats,
    Otherwise : TypeError (matrix must be a matrix list of integers or floats)

    The row of the matrix must be of the same size,
    Otherwise : TypeError (Each row of the matrix must have the same size)

    div must be a integer or float,
    Otherwise : TypeError (div must be a number)
    
    div can't be aqual to 0, Otherwise : ZeroDivisionError  (division by zero)

    Returns a new matrix
    """

    if not all(isinstance(row, list) and all(isinstance(item, (int, float))
    for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div ==  0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div,  2) for item in row] for row in matrix]
