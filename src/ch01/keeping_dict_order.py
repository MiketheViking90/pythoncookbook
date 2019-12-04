from collections import OrderedDict
from operator import itemgetter

d = OrderedDict()
d['d'] = 8.9
d['a'] = 10
d['b'] = 312
d['c'] = 83

print(d)

d = {
    'z':8,
    'f':12,
    'c':9,
    'a':33,
    'g':100,
}

d_sorted = OrderedDict(sorted(d.items(), key=itemgetter(0)))
print(d_sorted)