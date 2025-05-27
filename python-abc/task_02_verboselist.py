#!/usr/bin/python3
'''
This module include a class that extends the Python list class
'''


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, item):
        super().extend(item)
        print(f"Extended [{item}] to the list")

    def remove(self, item):
        super().remove(item)
        print(f"Remove [{item}] from the list")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item
