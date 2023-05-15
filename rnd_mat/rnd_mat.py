__author__ = "temso"

import numpy as np

# create int matrix
mat_int = np.random.randint(0, 10, (10, 4))
print(f'int matrix:\n{mat_int}\n')

# create float matrix
mat_float = np.random.rand(10, 4)
print(f'float matrix:\n{mat_float}\n')

# create float matrix rounded to 2 values
mat_float_round = np.round(np.random.rand(5, 2), 2)
print(f'rounded float matrix:\n{mat_float_round}\n')
