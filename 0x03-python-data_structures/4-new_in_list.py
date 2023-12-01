#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght_of_list = len(my_list)
    new_list = my_list.copy()
    if lenght_of_list == 0 or idx < 0 or idx >= lenght_of_list:
        return my_list
    else:
        new_list[idx] = element
        return new_list
