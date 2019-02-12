from bs4 import BeautifulSoup
from http import simple_get
from article import Article
from market import Market

def get_offers():
    market = Market('rewe')


    types = [None, 'fruehstueck', 'topangebote', 'obst-und-gemuese', 'frisch-und-kuehlung', 'tiefkuehl',
             'kochen-und-backen',
             'suessigkeiten', 'getraenke', 'drogerie', 'sonstige-angebote']

    labels = []
    for type in types:
        type = type + '/' if type != None else ''
        url = 'https://www.rewe.de/angebote/1931138/'+ type +'berlin/rewe-clayallee-336'
        raw_html = simple_get(url)
        if raw_html is None:
            continue
        html = BeautifulSoup(raw_html, 'html.parser')
        for div in html.select('div'):
            if div.get('class') is not None and 'drm-item-card' in div.get('class'):
                article = Article()

                #label
                for innerdiv in div.select('p'):
                    if innerdiv.get('class') is not None and 'headline' in innerdiv.get('class'):
                        article.label = innerdiv.getText()
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
                if article.label != None and article.label not in labels:
                    market.articles.append(article)
                    labels.append(article.label)

    return market