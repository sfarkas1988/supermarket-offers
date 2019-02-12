import requests
from article import Article
from market import Market
import json
import re
from datetime import datetime

def get_offers():
    response = requests.get("https://www.edeka.de/eh/service/eh/ods/offers?marketId=8001350&limit=89899")
    jsonData = json.loads(response.text)

    market = Market("edeka")
    market.valid_from = datetime.utcfromtimestamp(jsonData['gueltig_von']/1000)
    market.valid_until = datetime.utcfromtimestamp(jsonData['gueltig_bis'] / 1000)

    for jsonArticle in jsonData['docs']:
        article = Article()
        article.label = jsonArticle['titel']
        article.price = jsonArticle['preis']
        article.url = jsonArticle['bild_app']


        result = re.search('\((.*)\)', jsonArticle['beschreibung'])
        if result != None:
            unit = result.group(1).split('=')
            article.unit = unit[0]
            article.price_unit = unit[1]

        market.articles.append(article)

    return market