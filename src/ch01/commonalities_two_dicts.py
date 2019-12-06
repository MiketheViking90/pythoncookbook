a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}


common_keys = a.keys() & b.keys()
print(common_keys)

print(a.items() & b.items())

c = {k:a[k] for k in a.keys() - {'a', 'y', 'z'}}
print(c)