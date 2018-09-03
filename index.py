from offers import *
import json

articles = edeka.get_offers()
#articles = rewe.get_offers()
#articles = aldi.get_offers()
for article in articles:
    print json.dumps(article.__dict__)