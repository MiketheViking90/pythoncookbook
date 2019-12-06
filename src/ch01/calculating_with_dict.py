from collections import OrderedDict
from operator import itemgetter

prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
}

min_price = min(prices.items(), key=itemgetter(1))
print(min_price)
max_price = max(prices.items(), key=itemgetter(1))
print(max_price)

sort_by_price = OrderedDict(sorted(prices.items(), key=itemgetter(1)))
print(sort_by_price)