#!/usr/bin/python3
'''
This module include a class that extends the buit-in iterator
obtained from the iter
'''


class CountedIterator:
    def __init__(self, iterable):
        self.__iterable = iter(iterable)
        self.__count = 0

    def get_count(self):
        return self.__count

    def __next__(self):
        try:
            item = next(self.__iterable)
            self.__count += 1
            return item
        except StopIteration:
            raise 