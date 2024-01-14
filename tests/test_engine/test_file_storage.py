#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def test_all_method(self):
        storage = FileStorage()
        all_objs = storage.all()
        self.assertTrue(isinstance(all_objs, dict))

    def test_new_method(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn('BaseModel.' + obj.id, storage.all())

    def test_save_method(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn('BaseModel.' + obj.id, data)

    def test_reload_method(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('BaseModel.' + obj.id, new_storage.all())

if __name__ == '__main__':
    unittest.main()
