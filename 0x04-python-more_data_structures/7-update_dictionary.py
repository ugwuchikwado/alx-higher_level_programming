#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    sorted_dic = {key: value}
    a_dictionary.update(sorted_dic)
    return (a_dictionary)
