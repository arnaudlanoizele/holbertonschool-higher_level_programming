#!/usr/bin/python3
"""Module to load an object from a JSON file"""


def load_from_json(filename):
    """Creates an object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
