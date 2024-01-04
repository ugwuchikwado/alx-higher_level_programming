#!/usr/bin/python3
class Rectangle:
 
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
  
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __draw_rectangle(self):

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += str(self.print_symbol)

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        rct1_area = rect_1.area()
        rct2_area = rect_2.area()

        if rct1_area >= rct2_area:
            return rect_1

        return rect_2

    def __str__(self):

        return self.__draw_rectangle()

    def __repr__(self):
  
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

