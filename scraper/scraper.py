__author__ = 'Artem Solbonov'
import mod


def main():
    html = mod.get_html('https://habr.com/ru/flows/develop/')
    authors = mod.get_article_author(html)
    dates = mod.get_article_date(html)
    mod.get_article_name(html, authors, dates)
    # extra.get_article_date(html)


if __name__ == '__main__':
    main()
