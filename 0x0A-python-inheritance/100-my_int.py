#!/usr/bin/python3
""" 
module that inherits from int:
"""


class MyInt(int):
    """ MyInt inherits from int"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other

