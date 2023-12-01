#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    value1 = 0
    value2 = 0
    if len(tuple_a) == 0:
        value1 = 0 + tuple_b[0]
        value2 = 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        value1 = tuple_a[0] + 0
        value2 = tuple_a[1] + 0
    else:
        temp_list_1 = list(tuple_a)
        temp_list_2 = list(tuple_b)

        if len(temp_list_1) == 1:
            temp_list_1.append(0)

        if len(temp_list_2) == 1:
            temp_list_2.append(0)

        if len(temp_list_1) > 2:
            temp_list_1 = temp_list_1[0:2]

        if len(temp_list_2) > 2:
            temp_list_2 = temp_list_2[0:2]

        final_tuple_1 = tuple(temp_list_1)
        final_tuple_2 = tuple(temp_list_2)
        value1 = final_tuple_1[0] + final_tuple_2[0]
        value2 = final_tuple_1[1] + final_tuple_2[1]
    new_tuple = (value1, value2)
    return new_tuple
