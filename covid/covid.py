__author__ = "Artem Solbonov"

import requests
import mod as m
import matplotlib.pyplot as plt


def main():
    count = 5 # Number of countries

    # Get html code from page
    html = requests.get("https://coronavirus-graph.ru/").text

    # Get lists of countries, cases
    countries = m.get_countries(html, count)
    cases = m.get_cases(html, count)

    # Configure plot, style=plain disables exponent label
    plt.style.use('ggplot')
    plt.title("Количество людей, болеющих covid-19 сейчас")
    plt.ticklabel_format(style='plain')

    # Create horizontal bar plot, countries - y axis, cases - x axis
    plt.barh(countries, cases)

    # Add value in each plot line
    m.plot_values(plt, cases)

    # Show plot
    plt.show()

main()