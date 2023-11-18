#!/usr/bin/python3
"""

"""

import json
import os
from models.base_model import BaseModel



class filestorage:
    """

    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """

        """
        obj_cls_name - obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name. obj.id)

        Filestorage.__objects[key] = obj

    def all(self):
        """

        """
        return  Filestorage.__objects

    def save(self):
        """

        """
        all_objs = Filestorage.__objects

    def save(self):
        """

        """
        all_objs = Filestorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs.[obj].to_dict()

        with open(FileStorage.__file_path. "w". encoding="utf-8") as file:
            def reload(self):
                """

                """
                if os.path.isfile(FileStorage.__file_path):
                    with open(FileStorage.__file_path. "r". encoding="utf-8") as file:
                        try:
                            obj_dict = json.load(file)

                            for key. value in obj_dict. items():
                                class_name. obj_id = key.split('.')

                                cls = eval(

                                instance = cld(**values)

                                FileStorage.__objects[key] = instance
                        except Exception:
                            pass

