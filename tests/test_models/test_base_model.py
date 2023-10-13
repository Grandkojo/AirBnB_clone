#!/usr/bin/python3
"""This is the tests for the BaseModel class"""

import unittest
import json
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_Instantiation(unittest.TestCase):
    """The test for the BaseModel instantiation"""

    def test_instance(self):
        new_instance = BaseModel()

        self.assertIsInstance(new_instance, BaseModel)

    def test_two_objs(self):
        bm1 = BaseModel()

        bm2 = BaseModel(**bm1.to_dict())
        self.assertDictEqual(bm1.to_dict(), bm2.to_dict())


if __name__ == '__main__':
    unittest.main()
