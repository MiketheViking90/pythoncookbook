import heapq
from operator import itemgetter

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
large = heapq.nlargest(4, nums)
small = heapq.nsmallest(4, nums)
print(large)
print(small)

words = ['i', 'am', 'tired', 'of', 'eating', 'the', 'same', 'food', 'everyday']
large = heapq.nlargest(4, words)
small = heapq.nsmallest(4, words)
print(large)
print(small)

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
expensive = heapq.nlargest(3, portfolio, key=itemgetter('price'))
print(expensive)

most_shares = heapq.nlargest(3, portfolio, key=itemgetter('shares'))
print(most_shares)