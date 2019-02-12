from bs4 import BeautifulSoup
from http import simple_get
from article import Article
from market import Market
import datetime

def next_day(given_date, weekday):
    day_shift = (weekday - given_date.weekday()) % 7
    return given_date + datetime.timedelta(days=day_shift)


def get_offers():
    market = Market("aldi")
    now = datetime.datetime.now()
    dates = [
        ['mo', now - datetime.timedelta(days=now.weekday())],
        ['do', next_day(now, 3)],
        ['fr', next_day(now, 4)],
        ['mo', next_day(now, 0)]
    ]

    types = ['angebote', 'aktion']
    for type in types:
        for obj in dates:
            url = 'https://www.aldi-nord.de/angebote/'+type+'-'+obj[0]+'-' + '{:02d}'.format(obj[1].day) + '-' + '{:02d}'.format(obj[1].month) + '.html'
            #print url
            raw_html = simple_get(url)
            if raw_html is None:
                continue

            html = BeautifulSoup(raw_html, 'html.parser')
            for div in html.select('div'):
                #label
                if 'mod-article-tile' in div.get('class'):
                    article = Article()
                    article.date = format(obj[1],"%Y-%m-%d")
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

                    market.articles.append(article)

    return market