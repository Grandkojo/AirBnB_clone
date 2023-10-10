#!/usr/bin/python3
""" A class BaseModel that defines all common methods for other classes """

import uuid
from datetime import datetime


class BaseModel:
    """This is the BaseModel for all the classes"""

    def __init__(self, *args, **kwargs):
        """The initiaalizor of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if not key.startswith("__"):
                    if key == "created_at":
                        self.__dict__[key] = datetime.fromisoformat(value)
                    elif key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """The string representation of the object format"""
        print(f"[{self.__class__.__name__} ({self.id}) self.__dict__]")

    def save(self):
        """updates the attribute `updated_at` with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary after the instane is called"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
