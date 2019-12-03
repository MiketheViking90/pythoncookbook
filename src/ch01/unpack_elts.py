from statistics import mean


def drop_first_last(grades):
    first, *mid, last = grades
    return mean(mid)

avg = drop_first_last([86, 99, 67, 100, 65, 98])
print(avg)

*trail, current = [6,4,98,77,6,4,3,45,7]
print(trail)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'whiskey'),
    ('beer', 3, 54)
]

for tag, *tail in records:
    print(tag)