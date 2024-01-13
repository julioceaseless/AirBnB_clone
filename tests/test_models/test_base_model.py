#!/usr/bin/python3
"""Unit tests for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """test class containing all unit test methods for BaseModel"""

    def test_init_(self):
        """ """
        bm = BaseModel()

        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_uuid(self):
        """ """
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """ """
        bm = BaseModel()

        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at(self):
        """ """
        bm = BaseModel()

        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()

        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict_method(self):
        """ """
        bm = BaseModel()
        bm_dict = bm.to_dict()

        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['id'], bm.id)
        self.assertEqual(bm_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

    def test_init_with_kwargs(self):
        """ """
        data = {
                'id': '12345abcde',
                'created_at': '2022-01-01T12:00:00.000000',
                'updated_at': '2022-01-02T12:30:00.000000',
                'new_attribute': 'some_value'
                }
        bm = BaseModel(**data)

        self.assertEqual(bm.id, '12345abcde')
        self.assertEqual(bm.created_at, datetime(2022, 1, 1, 12, 0))
        self.assertEqual(bm.updated_at, datetime(2022, 1, 2, 12, 30))
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertTrue(hasattr(bm, 'new_attribute'))
        self.assertEqual(bm.new_attribute, 'some_value')

    def test_str_(self):
        """ """
        bm = BaseModel()
        bm.new_attribute = 'new_value'
        bm.another_attribute = 56

        expected_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)

        self.assertEqual(str(bm), expected_str)


if __name__ == "__main__":
    unittest.main()
