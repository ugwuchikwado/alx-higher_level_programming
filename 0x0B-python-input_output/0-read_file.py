#!/usr/bin/python3
""" 
Module that reads from a file 
"""


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename
    """

    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
        print(data, end='')

