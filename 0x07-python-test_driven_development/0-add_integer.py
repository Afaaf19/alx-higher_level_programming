#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """sum of two integers or floats
    Args:
    a: value number 1
    b: value number 2

    Raises:
    TypeError: if either a or b were neither float nor int

    Returns:
    a+b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
