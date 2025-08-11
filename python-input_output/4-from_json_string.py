#!/usr/bin/python3
"""Module for JSON string to object"""


def from_json_string(my_str):
    """Convert a JSON string to a Python object"""
    import json
    return json.loads(my_str)
