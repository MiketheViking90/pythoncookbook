import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

negs = [math.pow(n, 2) for n in mylist if n < 0]
negs_gen = (n for n in mylist if n < 0)


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

negs_custom = list(filter(is_int, mylist))
print(negs)
print(negs_gen)
print(negs_custom)

clip_neg = negs = [n if n < 0 else 0 for n in mylist]
print(clip_neg)

mask = [True, True, False]
nums = [1,2,3,4,5]

print(list(compress(nums, mask)))