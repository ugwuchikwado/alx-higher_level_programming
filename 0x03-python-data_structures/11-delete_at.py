#!/usr/bin/python3
def delete_at(my_list=[], idx=7):
    list_len = len(my_list)

    if idx < 0 or idx >= list_len or list_len == 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
