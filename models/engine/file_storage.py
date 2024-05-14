#!/usr/bin/python3
import json
import os
"""Module for FileStorage class"""
class FileStorage():
    """Class for storing and retrieving"""
    __file_path= "file.json"
    __objects={}

    def all(self):
        """Returns the object storing data """
        return FileStorage.__objects
    def new(self,obj):
        """creating __objects"""
        key= "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key]= obj

    def save(self):
        """Serializing the __objects"""
        serialised_objects={}
        for (key,value) in FileStorage.__objects.items():
            serialised_objects[key]= value.to_dict()
        
        with open(FileStorage.__file_path,"w") as file:
            json.dump(serialised_objects,file)


    def classes(self):
        """Importing classes of the whole project"""
        from models.base_model import BaseModel
        classes={
            "BaseModel": BaseModel
        }
        return classes
    def reload(self):
        """deserializing the __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                loaded_objects = json.load(file)
                new_objects = {}
                for key, value in loaded_objects.items():
                    obj_id = key
                    class_name = value["__class__"]
                    cls = self.classes()[class_name]
                    del value["__class__"]
                    obj = cls(**value)
                    new_objects[obj_id] = obj

                FileStorage.__objects = new_objects
