__author__ = "Artem Solbonov"

import requests
from bs4 import BeautifulSoup
import mod as m
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    count = 5 # Number of countries

    # Get all html code from page
    html = requests.get("https://coronavirus-graph.ru/").text

    # Get lists of countries and covid cases, count - countries number
    countries = m.get_countries(html, count)
    cases = m.get_cases(html, count)

    # Change plot ui style and title
    plt.style.use('ggplot')
    plt.title("Количество людей, болеющих covid-19 сейчас")

    # Configure the ScalarFormatter, useOffset not/show original numbers, style - on/off exponent
    plt.ticklabel_format(useOffset=False, style='plain')

    # Create horizontal bar plot, countries - y axis, cases - x axis
    plt.barh(countries, cases)

    # Adding values in each plot lines by plt.text
    for index, value in enumerate(cases):
        plt.text(value, index, str(value))

    # Building plot
    plt.show()

main()