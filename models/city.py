#!/usr/bin/python3
"""This has a class that inherits from Basemodel"""


from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""
    state_id = ""
    name = ""
