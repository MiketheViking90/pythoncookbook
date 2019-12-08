from operator import attrgetter
from pprint import pprint


class User:

    def __init__(self, id):
        self._id = id

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


users = [
    User(23),
    User(3),
    User(17),
    User(192),
    User(54)
]
by_id = sorted(users, key=attrgetter("_id"))
pprint(by_id)