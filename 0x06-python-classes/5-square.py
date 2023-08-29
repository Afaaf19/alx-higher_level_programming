#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class that  defines a square with a private attribute size,
    a public method area,
    getter and setter methods,
    and a public instance method called my_print that
    prints the square to stdout.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
        size (int): The size of the new square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """Computes and returns the area of the current square.
        Returns: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

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
