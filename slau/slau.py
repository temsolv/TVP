"""2x + 5y = 1
   x - 10y = 3 
"""

__author__ = "Artem Solbonov"

import numpy as np
import mod

def main():
    rows = 2 # Matrix rows number
    cols = 2 # Matrix columns number

    # Define left side of equation - matrix, filled by zeros
    matrix = np.zeros((rows, cols))

    # Fill matrix by entered values
    mod.fill_matrix(matrix, rows, cols)

    # Define right side of equation - vector, filled by zeros
    vector = np.zeros([rows])

    # Fill vector by entered values. Vector length always equal to rows number
    mod.fill_vector(vector)

    # Solve the equation by linalg.solve which takes two parameters - a matrix and a vector
    result = np.linalg.solve(matrix, vector)
    print(result)

main()