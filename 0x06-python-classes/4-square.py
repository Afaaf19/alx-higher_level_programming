#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class that uses a private attribute size,
    a public method area
    and getter and setter methods
    """
    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
        size (int): size of the new square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.__size = size

    def area(self):
        """Computes and returns the area of the current square.
        Returns: the area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the size of the square
        Returns: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """updates the size of the square
        Args:
        value (int): New size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
