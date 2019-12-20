from fnmatch import fnmatch

is_match = fnmatch('foo.txt', '*.txt')
print(is_match)

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
csvs = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(csvs)


addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
]

streets = [addr for addr in addresses if fnmatch(addr, '* ST')]
print(streets)

over_5000 = [a for a in addresses if fnmatch(a, '[2]* ST')]
print(over_5000)