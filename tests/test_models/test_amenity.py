#!/usr/bin/python3
"""Test for Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
