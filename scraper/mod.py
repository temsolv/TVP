__author__ = "Artem Solbonov"

import requests
from bs4 import BeautifulSoup


def get_articles(html, authors, dates):
    """ Function takes array with authors, dates and matches them with articles titles"""

    soup = BeautifulSoup(html, 'lxml') # Object of bs4 for scpapping
    articles = soup.find_all("a", class_="tm-title__link") # List of tags with selected class

    # Display info about article, author, date. Span.text - each article title
    for i, v in enumerate(articles):
        title = v.find("span").text
        print("\n", "Название: ", title, "\n",
              "Автор: ",authors[i].strip(), "\n",
              "Дата:", dates[i].strip(), "\n"*2)


def get_authors(html):
    """ Method that finds name of all authors and adding it on array, then return it"""

    soup = BeautifulSoup(html, 'lxml') # Object of bs4 for scpapping
    authors_tags = soup.find_all('a', class_='tm-user-info__username') # List of tags with selected class
    authors = [] # List of getted authors

    # Add each author name converted so string, in list
    for author in authors_tags:
        name = str(author.text)
        authors.append(str(name))
    return authors


def get_dates(html):
    """ Method that finds date of all articles and adding it on array, then return it"""

    soup = BeautifulSoup(html, 'lxml') # Object of bs4 for scpapping
    dates_tag = soup.find_all('time') # List of every time tags
    dates = [] # List of getted dates

    # Add each date to list
    for date in dates_tag:
        dates.append(date['title'])
    return dates