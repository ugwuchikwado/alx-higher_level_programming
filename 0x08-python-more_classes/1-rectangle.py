#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
   
        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):
   
        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
 
        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        if value >= 0:
            return True

        return False

