#!/usr/bin/python3
"""testing module
"""


def matrix_divided(matrix, div):
    """Divide a matrix"""
    if (type(matrix) is not list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    list_size = len(matrix[0])
    for i in matrix:
        if (len(i) is not list_size):
            raise TypeError("Each row of the matrix must have the same size")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    matrix2 = []
    for i in matrix:
        line = []
        for j in i:
            line.append(round((j / div),2))
        matrix2.append(line)
    return matrix2
