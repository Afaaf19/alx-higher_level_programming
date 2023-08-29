#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class that uses two private attribute size and position,
    two public methods area and my_print
    and getter and setter methods
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieves the size of the square
        Returns: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
        value (int): New size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.

        Returns: None.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square
        Returns:
        tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
        value (tuple): position of the square

        Raises:
        TypeError: if position is not a tuple of two positive integers.

        Returns: None
        """

        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes and returns the area of the current square.
        Returns: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
