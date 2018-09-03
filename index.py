import rewe
import aldi_offers

#
# articles = {
#     'Zwiebeln': [
#         'https://shop.rewe.de/p/speisezwiebeln-1kg-netz/1041138'
#     ],
#     'Tomaten': [
#         'https://shop.rewe.de/p/rewe-bio-rispentomaten-500g/1041181'
#     ]
# }
#
#
# for title in articles:
#     for link in articles[title]:
#         article = None
#         if 'rewe' in link:
#             article = rewe.get(link)
#         if article is not None:
#             print article.label
#             print article.price
#             print " "
#

articles = aldi_offers.get_offers()
print len(articles)
for article in articles:
    print article.label
    print article.price
    print article.url