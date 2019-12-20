from decimal import Decimal

a = 4.2
b = 2.1
print(a+b)

a = Decimal('4.2')
b = Decimal('2.1')
c = a + b
print(c)
print(c == 6.3)
print(c == Decimal('6.3'))
