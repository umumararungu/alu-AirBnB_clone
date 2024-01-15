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
        with open(FileStorage.__file_path, "w", encoding="utf-8")as file:
            json.dump(dict_obj,file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dict_obj = json.load(file)
                    for key,value in dict_obj.items():
                        class_name, obj_id = key.split('.')
                        class_ =eval(class_name)
                        instance = class_(**value)
                        FileStorage.__objects[key] = instance 
                except Exception:
                    pass           

