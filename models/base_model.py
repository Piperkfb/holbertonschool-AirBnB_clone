#!/usr/bin/python3
"""The base model for the clone"""
from datetime import datetime
import uuid


class BaseModel(object):
    def __init__(self):
        """Initilizing the attributes"""
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