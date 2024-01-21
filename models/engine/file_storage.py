#!/usr/bin/python3
"""
file storage
"""
import json
import os

from  models.base_model import BaseModel
from models.user import User

class FileStorage():
    """
    class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return what we have in storage"""
        return FileStorage.__objects
    
    def new(self,obj):
        """adding new object"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        """
        all_obj = FileStorage.__objects
        dict_obj = {}
        for obj in all_obj.keys():
            dict_obj[obj] = all_obj[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8")as file:
            json.dump(dict_obj,file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dict_obj = json.load(file)
                    for key, value in dict_obj.items():
                        class_name, obj_id = key.split('.')
                        class_ =eval(class_name)
                        instance = class_(**value)
                        FileStorage.__objects[key] = instance 
                except Exception:
                    pass           