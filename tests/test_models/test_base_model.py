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

    def test_with_one_arg(self):
        new = BaseModel(15)

        self.assertIsInstance(new, BaseModel)
        self.assertTrue(issubclass(type(new), BaseModel))
        self.assertEqual(str(type(new)),
                         "<class 'models.base_model.BaseModel'>")

    def test_two_objects(self):
        new1 = BaseModel()
        new2 = BaseModel(**new1.to_dict())

        self.assertDictEqual(new1.to_dict(), new2.to_dict())


if __name__ == '__main__':
    unittest.main()
