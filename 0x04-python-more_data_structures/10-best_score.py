#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    mKey = None
    mVal = None

    for i, j in a_dictionary.items():
        if mKey is None or j > mKey:
            mKey = j
            mVal = i

    return mVal
