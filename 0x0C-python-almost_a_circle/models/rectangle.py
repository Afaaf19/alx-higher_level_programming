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
        self. _verify_integer("x", val)
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

    def area(self):
        """calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """Returns a string that represents the rectangle"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the rectangle"""
        argc = len(args)
        kwargc = len(kwargs)
        assign_attr = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, assign_attr[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in assign_attr:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
