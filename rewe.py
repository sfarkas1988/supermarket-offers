# coding=utf-8
from bs4 import BeautifulSoup
from http import simple_get
from article import Article

def get(url):
    print url
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    price = None
    label = None
    for mark in html.select('mark'):
        if 'rs-qa-price' in mark.get('class'):
            string = mark.getText().encode("utf-8")
            print string
            price = float(string.replace("ab", "").replace("€", "").replace(" ", "").replace(",", "."))

    for h1 in html.select('h1'):
        if 'pd-QuickInfo__heading' in h1.get('class'):
            label = h1.getText()

    return Article(label, price, url)


