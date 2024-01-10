#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    int_val = 0

    for ch in roman_string:
        value = romans[ch]
        if (value > prev):
            value = value - (prev * 2)

        int_val += value
        prev = romans[ch]

    return int_val
