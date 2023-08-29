#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """The class square uses a private attribute size"""
    def __init__(self, size):
        """ Initializes a new square
        Args:
        size: size of the new square
        """
        self.__size = size
        
