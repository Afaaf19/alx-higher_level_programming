#!/usr/bin/python3
"""
model that contains a base class
"""
from os import path
import json
from json import dumps, loads


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
