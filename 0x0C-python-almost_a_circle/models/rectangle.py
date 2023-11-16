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
    def width(self, val):
        """set the width of the rectangle"""
        self._verify_integer("width", val, False)
        self.__width = val

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        """set the height of the rectangle."""
        self._verify_integer("height", val, False)
        self.__height = val

    @property
    def x(self):
        """get the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        """set the x of the rectangle."""
        self. _verify_integer("x",val)
        self.__x = val

    @property
    def y(self):
        """get the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        """set the y of the rectangle."""
        self._verify_integer("y", val)
        self.__y = val

    def _verify_integer(self, name, val, eq=True):
        """
        verify the value of an integer if it's an integer and validate it
        """
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and val < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and val <= 0:
            raise ValueError("{} must be > 0".format(name))
