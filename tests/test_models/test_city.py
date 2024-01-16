#!/usr/bin/python3
"""Test for user"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_inheritance(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))


if __name__ == '__main__':
    unittest.main()
