#!/usr/bin/python3
""" 
Module that defines the class Student
"""


class Student:
    """
    Class to create student instances
    """

    def __init__(self, first_name, last_name, age):
        """ 
        Special method to initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that returns directory description
        """
        obje = self.__dict__.copy()
        if type(attrs) is list:

            for items in attrs:
                if type(items) is not str:
                    return obje

            d_list = {}

            for iattr in range(len(attrs)):
                for datr in obje:
                    if attrs[iattr] == datr:
                        d_list[datr] = obje[datr]
            return d_list

        return obje

    def reload_from_json(self, json):
        """ 
        Replaces all attributes of the Student instance 
        """
        for attr in json:
            self.__dict__[atr] = json[atr]
