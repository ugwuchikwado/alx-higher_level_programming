#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    new_dic.update(a_dictionary)
    for key, value in new_dic.items():
        data = {key: (value * 2)}
        new_dic.update(data)
    return new_dic

