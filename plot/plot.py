__author__ = "Artem Solbonov"

import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import mod

def main():
    sample_frequency = 800 # In 1 second, we reading signal for 800 times
    common_frequency = 5 # Number of times one signal is processed per second
    samples = 700 # Number of frames in the signal
    multiplication_factor = 0.0008 # Multiplier for noise since noise is small

    # rnd.sample returns 0, 1000 length list of random elements from samples
    noise = rnd.sample(range(0, 1000), samples)

    # Reduce noise values using multiplication on factor
    mod.reduce_noise(noise, multiplication_factor)

    # Vector of samples from 0, to 700
    x = np.arange(samples)

    # Vector of y values, according to the formula
    y = np.sin(2*np.pi*common_frequency*x/sample_frequency) + noise

    # Naming plot
    plt.title("Signal sin wave")
    plt.xlabel("Samples")
    plt.ylabel("Sin value")

    # Source data to the plot
    plt.plot(x, y)

    # Show plot
    plt.show()

main()