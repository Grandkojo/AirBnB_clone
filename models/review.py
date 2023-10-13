#!/usr/bin/python3
"""This has a class that inherits from Basemodel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    place_id = ""
    user_id = ""
    text = ""
