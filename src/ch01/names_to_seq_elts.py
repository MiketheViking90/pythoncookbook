from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['email', 'join_date'])
sub1 = Subscriber('billy@gmail.com', '2012-10-23')
sub2 = Subscriber('yam@gmail.com', '2010-12-12')

print(sub1.email)
print(sub2.join_date)

email, _ = sub1
print(email)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s1 = Stock('APPL', 100, 82.94)
print(s1.shares)
s1 = s1._replace(name='FB')
print(s1)