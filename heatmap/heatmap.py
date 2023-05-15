__author__ = 'temso'

import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

# create matrix of random values
matrix = np.random.randint(0, 10, size=(6, 6))

# create heatmap
sb.heatmap(matrix, cmap="rocket", annot=True)

# show heatmap
plt.show()
