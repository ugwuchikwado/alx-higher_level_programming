#!/usr/bin/python3
def no_c(my_string):
    str_without_c = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            str_without_c += c
    return str_without_c
