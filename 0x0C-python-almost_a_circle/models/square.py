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

    def update(self, *args, **kwargs):
        """updates the attributes of the square"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
