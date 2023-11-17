#!/usr/bin/python3
"""
model that contains a base class
"""
from os import path
import json
from json import dumps, loads
import csv


class Base:
    """
    Base class created in order to manage id attribute in future classes"
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dict):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dict is None or len(list_dict) == 0:
            return '[]'
        return dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_obj):
        """
        writes the JSON string representation of list_objs
        """
        if list_obj is not None:
            list_obj = [o.to_dictionary() for o in list_obj]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            inst = Rectangle(1, 1)
        elif cls is Square:
            inst = Square(1)
        else:
            inst = None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
         returns a list of instances
        """
        fname = cls.__name__ + '.json'
        if not path.exists(fname):
            return []

        with open(fname, mode='r', encoding='utf-8') as file:
            objs = cls.from_json_string(file.read())
            inst = [cls.create(**elem) for elem in objs]
            return inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes and deserializes in CSV
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)
