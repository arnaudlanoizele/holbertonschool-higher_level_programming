#!/usr/bin/python3
"""this module provides a function that creates an object from a JSON"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file
    Args:
        filename: The file to check
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
