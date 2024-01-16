#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        """ """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes(self):
        """ """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save_method(self):
        """ """
        obj = BaseModel()
        created_at_before_save = obj.created_at
        obj.save()
        updated_at_after_save = obj.updated_at
        self.assertNotEqual(created_at_before_save, updated_at_after_save)

    def test_to_dict_method(self):
        """ """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if __name__ == '__main__':
    unittest.main()
