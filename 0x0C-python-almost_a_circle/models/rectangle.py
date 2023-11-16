#!/usr/bin/python3
"""
model that defines the Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class: subclass of Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = w

    @property
    def width(self):
        """ width of the rectangle: getter"""
        return self.__width

    @width.setter
    def width(self, val):
        """width of the rectangle: setter"""
        self.__width = val

    @property
    def height(self):
        """height of the rectangle: getter"""
        return self.__height

    @height.setter
    def height(self, val):
        """height of the rectangle: setter"""
        self.__height = val

    @property
    def x(self):
        """x of the rectangle: getter"""
        return self.__x

    @x.setter
    def x(self, val):
        """
        x of the rectangle: setter
        """
        self.__x = val

    @property
    def y(self):
        """y of the rectangle: getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """y of the rectangle: setter"""
        self.__y = val
