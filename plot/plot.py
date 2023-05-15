__author__ = 'temso'

import numpy as np
import matplotlib.pyplot as plt

# create data for plot
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)

# name axis
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("sin(x), cos(x), -x")

# grid off and plot show
plt.grid(False)
plt.show()
