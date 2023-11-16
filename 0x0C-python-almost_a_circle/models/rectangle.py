#!/usr/bin/python3
"""
module defining the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    rectangle class, a subclass of Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes a Rectangle instance.
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, param):
        """set the width of the rectangle"""
        self.__width = param

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, param):
        """set the height of the rectangle."""
        self.__height = param

    @property
    def x(self):
        """get the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, param):
        """set the x of the rectangle."""
        self.__x = param

    @property
    def y(self):
        """get the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, param):
        """set the y of the rectangle."""
        self.__y = param
