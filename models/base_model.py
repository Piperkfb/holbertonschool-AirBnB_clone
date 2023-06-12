#!/usr/bin/python3
"""The base model for the clone"""
from datetime import datetime
import uuid


class BaseModel(object):
    def __init__(self, *args, **kwargs):
        """Initilizing the attributes"""
        if kwargs:
            dateform = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], dateform)
            self.__dict__ = k_dict
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """Return formated string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, 
                         self.id, self.__dict__)
    def save(self):
        """Updates update_at with current time"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Dict of all keys and values"""
        newdict = self.__dict__.copy()
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        newdict["__class__"] = self.__class__.__name__
        return newdict