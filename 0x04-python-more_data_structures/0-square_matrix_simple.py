#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = matrix.copy()
    for i in range(len(m)):
        m[i] = list(map(lambda x: x**2, m[i]))
    return(m)
