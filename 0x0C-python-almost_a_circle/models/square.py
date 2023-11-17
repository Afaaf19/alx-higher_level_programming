#!/usr/bin/python3
"""
module that defines the square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class, subclass of Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string that represents the rectangle"""
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter of size square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size square"""
        self.width = value
        self.height = value
