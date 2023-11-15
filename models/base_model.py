#!/usr/bin/python3

import models
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs, items():
                if key == "__class__":
                    continue
                elif key == "create_at" or key == "updated_at":
                    setattr(self. key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())

                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()

            models.storage.new(self)

    def __setattr__(self, name, value):
        """

        """
        if name in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, '%y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    raise AttributeError("Invalid value: ({}) for name: ({})"
                                         .format(value, name))
        super().__setattr__(name, value)

    def __str__(self):
        """

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name. self.id. self.__dict__)

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

        

    def to_dict(self):
        """

        """
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["__class__"] = self.__class__.__name__
        
        return inst_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_FIrst_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
