#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)

    if list_len == 0:
        return None
    else:
        max_number = my_list[0]
        for n in my_list:
            if n > max_number:
                max_number = n

        return max_number
