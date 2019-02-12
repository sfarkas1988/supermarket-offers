from offers import *
import json

offers = [
    edeka.get_offers(),
    rewe.get_offers(),
    aldi.get_offers()
]


for market in offers:
    print '=> '+ market.name\
        #, market.valid_from, market.valid_until
    for article in market.articles:
        print json.dumps(article.__dict__)

#https://github.com/tryolabs/luminoth
#https://www.tensorflow.org/install/install_mac