#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data"""
        self.size = size

    def area(self):
        """Returns current square area"""
        return self.__size**2

    @property
    def size(self):
        """Get data"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set data"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __lsth__(self, other):
        return self.area() < other.area()

    def __lseq__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __noeq__(self, other):
        return self.area() != other.area()

    def __grth__(self, other):
        return self.area() > other.area()

    def __greq__(self, other):
        return self.area() >= other.area()
