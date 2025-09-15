#!/usr/bin/python3
"""
Description: This module contains a class Student that defines a student by
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.fist_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            my_dict = {}
            for attr in sorted(attrs):
                if hasattr(self, attr):
                    my_dict[attr] = getattr(self, attr)
                return my_dict
            else:
                return self.__dict__
