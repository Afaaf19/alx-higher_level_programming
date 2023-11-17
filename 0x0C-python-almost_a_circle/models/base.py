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
