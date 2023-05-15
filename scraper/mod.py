__author__ = 'Artem Solbonov'
import requests
from bs4 import BeautifulSoup


# Get articles names
def get_article_name(html, authors_list, datetimes):
    """ Function takes array with author names and matches them with articles titles"""
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('a', class_='tm-article-snippet__title-link')
    i = 0
    for article in articles:
        article_name = article.find('span').text
        print("Article:", i)
        print("Author:", authors_list[i])
        print("Title:", article_name)
        print("Date:", datetimes[i])
        print("------------------------------------------------------")
        i += 1


# Get articles authors
def get_article_author(html):
    """ Function finds name of all authors and adding it on array"""
    soup = BeautifulSoup(html, 'lxml')
    authors = soup.find_all('a', class_='tm-user-info__username')
    authors_list = []
    for author in authors:
        author_name = str(author.text)
        authors_list.append(str(author_name))
    return authors_list


# Get article date
def get_article_date(html):
    """ Function finds date of all articles and adding it on array"""
    soup = BeautifulSoup(html, 'lxml')
    times = soup.find_all('time')
    datetimes = []
    for time in times:
        datetimes.append(time['title'])
    return datetimes


# Returns page in txt
def get_html(url):
    """ Function taking page by url and return it in txt"""
    result = requests.get(url)
    return result.text
