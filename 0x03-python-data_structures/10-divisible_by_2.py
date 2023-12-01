#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_lenght = len(my_list)
    for n in range(0, list_lenght):
        if my_list[n] % 2 != 0:
            my_list[n] = False
        else:
            my_list[n] = True
    return my_list
