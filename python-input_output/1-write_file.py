#!/usr/bin/python3
"""Module for writing to a text file"""


def write_file(filename="", text=""):
    """Writes a UTF-8 encoded text to a file and returns
    the number of characters written

    Args:
        filename (str): The name of the file to write to.
        Defaults to empty string
        """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
