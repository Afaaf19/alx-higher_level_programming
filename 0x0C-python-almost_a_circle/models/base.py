#!/usr/bin/python3
"""
model that contains a base class
"""

class Base:
    """
    Base class created in order to manage id attribute in all my future classes of this project
    """

    __nb_objects = 0

    def __nb_objects(self, id=None):
        """
        Constructor
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id