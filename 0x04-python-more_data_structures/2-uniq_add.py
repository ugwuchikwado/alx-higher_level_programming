#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_sum = 0
    for i in set(my_list):
        list_sum += i
    return list_sum

