from bs4 import BeautifulSoup
from http import simple_get
from article import Article

def get_offers():
    raw_html = simple_get('https://www.aldi-nord.de/angebote/aktion-mo-03-09.html')
    html = BeautifulSoup(raw_html, 'html.parser')
    articles = []
    for div in html.select('div'):
        #label
        if 'mod-article-tile' in div.get('class'):
            label = None
            price = None
            url = None
            # title
            h4 = div.select('h4')
            for tag in h4:
                label = tag.getText()

            # price
            span = div.select('span')
            for sp in span:
                if sp.get('class') is not None and 'price__main' in sp.get('class'):
                    price = float(sp.getText().replace("*", "").lstrip("\n").rstrip("\n"))

            #url
            a = div.select('a')
            for href in a:
                if (href.get('class') is not None and 'mod-article-tile__action' in href.get('class')):
                    url = 'https://www.aldi-nord.de/' + href.get('href')
            articles.append(Article(label, price, url))
    return articles