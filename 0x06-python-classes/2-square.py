#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class uses a private attribute size"""
    def __init__(self, size=0):
        """Inisializes a new square.
        Args:
        size (int): size of the new square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
