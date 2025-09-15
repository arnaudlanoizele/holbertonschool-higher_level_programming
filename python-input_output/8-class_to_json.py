#!/usr/bin/python3

"""
Description : This module contain a script that returns the dictionnary
description with simple data structure (List, dictionary, string, integer)
"""


def class_to_json(obj):
    """
    A funtion that returns the dictionnary description with simple data
    structure (list, dictionary, string, integer)
    """
    return obj.__dict__
