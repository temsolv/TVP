__author__ = "Artem Solbonov"

import numpy as np
import seaborn as sb
import matplotlib.pylab as plt


def main():
    # Generate 10x10 random integer matrix
    data = np.random.rand(10, 10)
    print("Our dataset is:", data)

    # Plot the heatmap, Create a new figure. Figsize - width, height
    plt.figure(figsize=(10,10))

     # Define plot title
    plt.title("Heatmap using Seaborn Method")

    # Initial of heatmap. Data - 2D dataset that can be coerced into an ndarray
    # linewidths - width of the lines that will divide each cell
    # annot - if True, write the data value in each cell
    # The color changes describe the relationship between two values according to the
    # intensity of the color in a particular block
    heatmap = sb.heatmap(data, linewidths=1, annot=True)
    
    plt.show()
main()