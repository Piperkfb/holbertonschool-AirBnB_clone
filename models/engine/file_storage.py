#!/usr/bin/python3
"""Storage"""
import json


class FileStorage(object):
    """Stores data as needed"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self,obj):
        """Sets __object to obj"""

    def save(self):

    def reload(self):