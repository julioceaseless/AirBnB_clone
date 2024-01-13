#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """ """
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        """ """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_new_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = 'BaseModel.{}'.format(obj.id)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            key = 'BaseModel.{}'.format(obj.id)
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_reload_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Create a new storage instance to simulate program restart
        new_storage = FileStorage()
        new_storage.reload()

        key = 'BaseModel.{}'.format(obj.id)
        self.assertIn(key, new_storage._FileStorage__objects)
        reloaded_obj = new_storage._FileStorage__objects[key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.to_dict(), obj.to_dict())

if __name__ == '__main__':
    unittest.main()

