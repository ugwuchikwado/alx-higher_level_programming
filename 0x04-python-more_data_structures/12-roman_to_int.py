#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str) or roman_string is None:
        return 0
    numb = 0
    temp = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for iter1 in roman_string:
        if temp >= int(dict.get(iter1)) and temp != 0:
            numb += int(dict.get(iter1))
        elif temp < int(dict.get(iter1)) and temp != 0:
            numb = numb + ((int(dict.get(iter1)) - temp) - temp)
        elif temp == 0:
            numb += int(dict.get(iter1))
        temp = int(dict.get(iter1))
    return (numb)

