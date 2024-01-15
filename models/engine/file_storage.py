#!/usr/bin/python3
"""
file storage
"""
import json
import os
from test_  models.base_model import BaseModel

class FileStorage():
    """
    class
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        """
        class_name_obj = obj.__class__.__name__
        key = "{}{}".format(class_name_obj,obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        """
        return FileStorage.__objects
    def save(self):
        """
        """
        all_obj = FileStorage.__objects
        dict_obj = {}
        for obj in all_obj.keys():
            dict_obj[obj].to_dict()


