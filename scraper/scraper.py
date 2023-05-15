__author__ = 'Artem Solbonov'
import extra


def main():
    html = extra.get_html('https://habr.com/ru/flows/develop/')
    authors = extra.get_article_author(html)
    dates = extra.get_article_date(html)
    extra.get_article_name(html, authors, dates)
    # extra.get_article_date(html)


if __name__ == '__main__':
    main()
