#!/usr/bin/python3
"""
Module that writes to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Args:
        filename: filename
        text: text to write

    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
