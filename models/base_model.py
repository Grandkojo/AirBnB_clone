#!/usr/bin/python3
""" A class BaseModel that defines all common methods for other classes """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the BaseModel for all the classes"""

    def __init__(self, *args, **kwargs):
        """The initializer of the class"""
        if kwargs:
            for k, v in kwargs.items():
                if not k.startswith("__"):
                    if k == "created_at" or k == "updated_at":
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[k] = datetime.strptime(v, date_format)
                    else:
                        self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The string representation of the object format"""
        return ("[{} ({}) {}]"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the attribute `updated_at` with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary after the instane is called"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
