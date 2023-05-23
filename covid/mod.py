__author__ = "Artem Solbonov"

from bs4 import BeautifulSoup


def get_countries(html, amt):
    """Method that finds countries from html code in selected amount"""

    soup = BeautifulSoup(html, "lxml") # Object of bs4 for scrapping
    tds = soup.find_all("td", class_="td_country") # List of td tags, with class td_country
    countries = [] # List of getted countries

    # Append to list every country name in range 1...(amt+1)
    for td in tds[1:amt+1]:
        # td.text - country name
        countries.append(td.text)
    return countries


def get_cases(html, amt):
    """Method that finds covid cases from html code in selected amount"""

    soup = BeautifulSoup(html, "lxml") # Object of bs4
    tds = soup.find_all("td", class_="td_rest") # List of td tags, with class td_rest
    cases = [] # Getted cases list

    # Append to list every case in range 1...(amt+1), 
    for td in tds[1:amt+1]:
        # Finds "b".text in each td, "b".text - case value
        cases.append(int((td.find("b").text).replace(" ", "")))
    return cases


def plot_values(plt, values):
    """Function that adds values to the each plot line"""
    for index, value in enumerate(values):
        plt.text(value, index, str(value))