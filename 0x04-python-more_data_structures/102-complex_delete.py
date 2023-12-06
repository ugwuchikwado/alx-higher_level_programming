#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_dict = []
    for key, value in a_dictionary.items():
        if value == value:
            temp_dict.append(key)
    for x in temp_dict:
        del a_dictionary[x]
    return a_dictionary

