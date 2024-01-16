#!/usr/bin/python3
"""Test for Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        place = Place()
        attributes = {"city_id": "", "user_id": "", "name": "",
                      "description": "", "number_rooms": 0,
                      "number_bathrooms": 0, "max_guest": 0,
                      "price_by_night": 0, "latitude": 0.0,
                      "longitude": 0.0, "amenity_ids": ""
                      }

        for k in attributes:
            self.assertTrue(hasattr(place, k))
            # self.assertIs(place.k, attributes[k])

    def test_inheritance(self):
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))


if __name__ == '__main__':
    unittest.main()
