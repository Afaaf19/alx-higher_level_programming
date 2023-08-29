#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class that uses a private attribute size
    and a public method area"""
    def __init__(self, size=0):
        """Initializes a new Square.
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

    def area(self):
        """Computes and returns the area of the current square.
        Returns: the area of the square.
        """

        return self.__size ** 2
