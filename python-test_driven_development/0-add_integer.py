#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function 'add_integer' takes two parameters
and returns their sum.
"""

def add_integer(a, b=98):
    """
    Return the sum of two integers.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
