#!/usr/bin/pytohn3
"""Module for appending to a text file"""


def append_write(filename="", text=""):
    """Appends a UTF-8 encoded text to a file and returns
    the number of characters added

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
