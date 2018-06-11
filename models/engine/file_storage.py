#!/usr/bin/env python3
""" This is a storage system for AirBnB project
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    """
    __file_path = 'file.json' #path to json file
    __objects = {} #dict to store id ex: (absemodel.21221212)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        filename = FileStorage.__file_path
        new_dict = {}
        for obj_key, obj in FileStorage.__objects.items():
            new_dict[obj_key] = obj.to_dict()
        with open(filename, mode='w', encoding='utf-8') as fileopen:
            json.dump(new_dict, fileopen)


    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file exists ; otherwise, do nothing)
        """
        filename = FileStorage.__file_path
        try:
            with open(filename, mode='r', encoding='utf-8') as fileopen:
                obj_l = json.load(fileopen)
                for i, x in obj_l.items():
                    self.new(eval(x["__class__"])(**x))
        except:
            pass

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects