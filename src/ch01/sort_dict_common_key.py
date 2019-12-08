from operator import itemgetter
from pprint import pprint

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    {'fname': 'Jill', 'lname': 'Thomas'},
    {'fname': 'Nate', 'lname': 'Nonong'},
    {'fname': 'Jesse', 'lname': 'Santiago'},
]

by_id = sorted(rows, key=lambda x: x.get('uid', 0))
by_lname = sorted(rows, key=itemgetter('lname'))
pprint(by_id)
pprint(by_lname)
