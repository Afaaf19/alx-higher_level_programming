#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        here = fct(*args)
        return (here)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None

