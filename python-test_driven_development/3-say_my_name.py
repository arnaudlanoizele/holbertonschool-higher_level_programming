#!/usr/bin/python3
"""
Module for printing names.
This module provides a single function that prints a name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a name
    Args:
        first_name: The first name to print
        last_name: The last name to print
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print(f"My name is {first_name} {last_name}")
