#!/usr/bin/python3
""" 
Module that inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    result = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            result += [line]
            if line.find(search_string) != -1:
                res += [new_string]

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(result))
