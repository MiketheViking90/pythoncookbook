from itertools import groupby
from operator import itemgetter
from pprint import pprint

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

def index_by_field(data):
    rows.sort(key=itemgetter('date'))
    groups = groupby(rows, key=itemgetter('date'))
    return {k: list(iter) for k, iter in groups}

date_index = index_by_field(rows)
pprint(dict(date_index))