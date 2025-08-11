#!/usr/bin/python3
"""Module for json string conversion"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj (object): The object to convert to JSON string

    Returns:
        str: The JSON string representation object"""
    import json
    return json.dumps(my_obj)
