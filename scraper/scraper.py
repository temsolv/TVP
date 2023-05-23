__author__ = "Artem Solbonov"

import mod
import requests

def main():
    # Get html code from page
    html = requests.get("https://habr.com/ru/flows/develop/").text

    # Get authors list
    authors = mod.get_authors(html)

    # Get dates list
    dates = mod.get_dates(html)

    # Show article information
    mod.get_articles(html, authors, dates)

main()