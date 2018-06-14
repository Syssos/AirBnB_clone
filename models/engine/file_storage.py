#!/usr/bin/env python3
""" This is a storage system for AirBnB project
"""
from models.base_model import BaseModel
from models.user import User
import json
import os


class FileStorage(object):
    """
    """
    __file_path = 'file.json' #path to json file
    __objects = {} #dict to store obj's ex: (absemodel.21221212)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        filename = FileStorage.__file_path
        new_dict = {}
        if self.__objects:
            for obj_key, obj in FileStorage.__objects.items():
                new_dict[obj_key] = obj.to_dict()
            with open(filename, mode='w', encoding='utf-8') as fileopen:
                json.dump(new_dict, fileopen)
        else:
            try:
                os.remove(self.__file_path)
            except FileNotFoundError:
                pass

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file exists ; otherwise, do nothing)
        """
        filename = self.__file_path
        try:
            with open(filename, mode='r', encoding='utf-8') as fileopen:
                obj_1 = {}
                obj_l = json.load(fileopen)
                for key, val in obj_l.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
        except:
            pass

    def all(self):
        """ Returns the dictionary __objects
        """
        return self.__objects