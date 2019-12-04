from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['c'].append(4)
d['c'].append(8)

print(d)

