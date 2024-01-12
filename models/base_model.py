#!/usr/bin/python3
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """recreate an instance from a dictonary representation"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            # if kwargs is empty, create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """
        serialize an object to dictionary Utilizes
        the __dict__ special object attribute
        """
        obj_to_dict = self.__dict__.copy()
        obj_to_dict['__class__'] = self.__class__.__name__
        obj_to_dict['created_at'] = self.created_at.isoformat()
        obj_to_dict['updated_at'] = self.updated_at.isoformat()
        return obj_to_dict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
