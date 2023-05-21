__author__ = "Artem Solbonov"

import numpy as np


def fill_matrix(matr: np.array, rows: int, cols: int):
    """Function that fills multidimensional array, of size rows and cols, with input values"""
    for i in range(rows):
        for j in range(cols):
            matr[i][j] = int(input(f"[{i}][{j}]="))


def fill_vector(vect: np.array):
    """Function that fills one-dimensional array, of length len, with input values"""
    for i in range(len(vect)):
        vect[i] = int(input(f"[{0}]="))