#!/usr/bin/python3
"""Module for writting an object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON reprentation"""
    import json
    with json.open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
