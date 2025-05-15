#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function 'add_integer' takes two parameters
and returns their sum.
"""
def add_integer(a, b=98):
    """
    Return the sum of two integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
