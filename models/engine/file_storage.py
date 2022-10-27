#!/usr/bin/python3
""" serializes instances of JSON file, deserializes JSON to instances """
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ file storage creation """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects """
        return self.__objects

    def new(self, obj):
        """ adds new object to __objects """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ saves objects to json file """
        JsonData = {}
        for key, value in self.__objects.items():
            JsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as wr:
            json.dump(JsonData, wr)

    def reload(self):
        """ reloads object from JSON file """
        try:
            with open(self. __file_path, 'r') as rd:
                data = json.load(rd)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass
        
