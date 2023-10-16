#!/usr/bin/python3
"""This is the tests for the BaseModel class"""

import unittest
import json
import re
import uuid
import os
from models.engine.file_storage import FileStorage
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

    def test_many_args(self):
        arguments = [i for i in range(2000)]
        bm = BaseModel(*arguments)

    def test_with_one_kwargs(self):
        bm = BaseModel(id="hello")
        self.assertIsInstance(bm, BaseModel)

    def test_with_more_kwargs(self):
        bm = BaseModel(name="Hello", id="re",
                       created_at="2017-09-28T21:03:54.052302",
                       updated_at="2018-09-28T21:03:54.052302")
        self.assertIsInstance(bm, BaseModel)

    def test_with_args_and_kwargs(self):
        bm = BaseModel(45, id="34")
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, "34")

    def test_no_args(self):
        bm = BaseModel()
        self.assertEqual(type(bm), BaseModel)

    # Testing the id
    def test_id_is_string(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_id_is_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

        lis = [BaseModel().id for i in range(2000)]
        self.assertEqual(len(lis), len(set(lis)))

    def test_id_list(self):
        bm = BaseModel(id=[])
        self.assertIsInstance(bm.id, list)

    def test_id_int(self):
        bm = BaseModel(id=45)
        self.assertEqual(bm.id, 45)

    def test_id_dictionary(self):
        self.assertEqual(BaseModel(id={"hi": 2}).id, {"hi": 2})

    def test_id_tuple(self):
        self.assertEqual(BaseModel(id=(2, 3)).id, (2, 3))

    def test_id_set(self):
        self.assertEqual(BaseModel(id={2, 3}).id, {2, 3})

    def test_id_float(self):
        self.assertEqual(BaseModel(id=3.3).id, 3.3)

    def test_id_complex(self):
        self.assertEqual(BaseModel(id=complex(2)).id, complex(2))

    def test_id_nan(self):
        import math
        self.assertTrue(math.isnan(BaseModel(id=float('nan')).id))

    def test_id_infinity(self):
        self.assertEqual(BaseModel(id=float('inf')).id, float('inf'))

    def test_id_bool(self):
        self.assertEqual(BaseModel(id=True).id, True)

    def test_id_byte(self):
        self.assertEqual(BaseModel(id=b"hello").id, b"hello")

    def test_id_negative(self):
        self.assertEqual(BaseModel(id=-3).id, -3)

    def test_id_zero(self):
        self.assertEqual(BaseModel(id=0).id, 0)

    def test_id_None(self):
        self.assertEqual(BaseModel(id=None).id, None)

    # Testing the created_at
    def test_created_at_normal_time(self):
        bm = BaseModel(created_at="2017-09-28T21:03:54.052302")
        self.assertIsInstance(bm.created_at, datetime)

    def test_created_at_wrong_wrong_year(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="0000-09-28T21:03:54.052302")

    def test_created_at_wrong_month(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2023-23-28T21:03:54.052302")
            self.bm.save()
            diff = self.bm.updated_at - datetime.now()
            self.assertTrue(all(isinstance(k, datetime)
                            for k in [prev_time, new_time]))
            self.assertNotEqual(prev_time, new_time)

            self.assertTrue(abs(diff.total_seconds()) < 0.1)


class TestBaseModel_Str(unittest.TestCase):
    """This is the test case for the __str__ method"""

    def test_len(self):
        bm = BaseModel()
        self.assertTrue(len(str(bm)) > 1)


if __name__ == '__main__':
    unittest.main()
