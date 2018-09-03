from bs4 import BeautifulSoup
from http import simple_get
from article import Article


def get_offers():
    raw_html = simple_get('https://www.edeka.de/eh/minden-hannover/edeka-colombino-sundgauer-str.-109/angebote.jsp')
    html = BeautifulSoup(raw_html, 'html.parser')
    articles = []

    print html

    return articles

