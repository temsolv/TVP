__author__ = "temso"

import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# create numpy matrix and convert to array
matrix = np.random.randint(0, 10, (10, 4))
array = np.asarray(matrix).ravel()

# create and show histogram
sb.histplot(data=array, color="red", kde=True)
plt.show()
