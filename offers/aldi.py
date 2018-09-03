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
            article = Article();
            # title
            h4 = div.select('h4')
            for tag in h4:
                article.label = tag.getText()

            # price
            span = div.select('span')
            for sp in span:
                if sp.get('class') is not None and 'price__main' in sp.get('class'):
                    article.price = float(sp.getText().replace('*', '').lstrip('\n').rstrip('\n'))
                if sp.get('class') is not None and 'price__base' in sp.get('class'):
                    article.price_unit = sp.getText().replace('(', '').replace(')', '').replace(' ', '')
                    splitted_unit = article.price_unit.split('=')
                    article.price_unit = splitted_unit[1]
                    article.unit = splitted_unit[0]

            #url
            a = div.select('a')
            for href in a:
                if (href.get('class') is not None and 'mod-article-tile__action' in href.get('class')):
                    article.url = 'https://www.aldi-nord.de/' + href.get('href')

            articles.append(article)
    return articles