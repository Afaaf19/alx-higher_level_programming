#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dictionary = {
            'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    res = 0
    prev_val = 0

    for ch in reversed(roman_string):
        val = roman_dictionary.get(ch, 0)
        if val >= prev_val:
            res += val
        else:
            res -= val
        prev_val = val
    return res
