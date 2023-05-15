__author__ = "temso"

import numpy as np

# matrix of coef before variables
coefs = np.random.randint(0, 10, (2, 2))

# free member vector
vector = np.random.randint(0, 10, (2))

# solving equation
out = np.linalg.solve(coefs, vector)
print(f'res: {out}')
