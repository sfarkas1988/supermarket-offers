from bs4 import BeautifulSoup
from http import simple_get
from article import Article

def get_offers():
    raw_html = simple_get('https://www.rewe.de/angebote/1931138/berlin/rewe-clayallee-336')
    html = BeautifulSoup(raw_html, 'html.parser')
    articles = []

    for div in html.select('div'):
        if div.get('class') is not None and 'drm-item-card' in div.get('class'):
            article = Article()

            #title
            span = div.select('span')
            if len(span) > 1:
                article.label = span[0].getText()

            # price
            for innerdiv in div.select('div'):
                if innerdiv.get('class') is not None and 'price-euro' in innerdiv.get('class'):
                    article.price = innerdiv.getText()
                elif innerdiv.get('class') is not None and 'price-cent' in innerdiv.get('class'):
                    article.price += innerdiv.getText()

            if article.price is not None:
                article.price = float(article.price.replace(',', '.'))

            text_description = div.select('.text-description')
            if len(text_description) > 0:
                for p in text_description[0].select('p'):
                    if '=' in p.getText():
                        article.price_unit = p.getText().replace('(', '').replace(')', '').replace(' ', '')
                        splitted_unit = article.price_unit.split('=')
                        article.price_unit = splitted_unit[1]
                        article.unit = splitted_unit[0]
                #unit_index = 0
                #if len(text_description) == 3:
                #    unit_index = 1
                #print text_description[unit_index].getText()


            # #url
            # a = div.select('a')
            # for href in a:
            #     if (href.get('class') is not None and 'mod-article-tile__action' in href.get('class')):
            #         article.url = 'https://www.aldi-nord.de/' + href.get('href')

            articles.append(article)
    return articles