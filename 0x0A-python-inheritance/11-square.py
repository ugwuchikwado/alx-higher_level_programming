#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    class Square inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
