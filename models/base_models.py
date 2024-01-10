#!/usr/bin/python3
from datetime import datetime


class BaseModel:
    def save(self):
        """
        update the public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        serialize an object to dictionary
        the __dict__ special attribute stores the
        object attributes and their values in dict format
        """
        obj_to_dict = self.__dict__.copy()
        obj_to_dict['__class__'] = self.__class__.__name__
        obj_to_dict['created_at'] = self.created_at.isoformat()
        obj_to_dict['updated_at'] = self.updated_at.isoformat()
        return obj_to_dict
