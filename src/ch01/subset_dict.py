from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

low_price = {k:v for k,v in prices.items() if v < 50}
pprint(low_price)

alpha = {k: v for k,v in prices.items() if k < 'm'}
print(alpha)