record = '0123456789012345678901234567890123456789012345678901234567890'

SHARES_SLICE = slice(20, 32)
PRICE_SLICE = slice(40, 42)

shares = record[SHARES_SLICE]
price = record[PRICE_SLICE]
cost = int(shares) * float(price)
print(cost)

print(SHARES_SLICE)