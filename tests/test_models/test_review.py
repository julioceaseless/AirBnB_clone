#!/usr/bin/python3
"""Test for user"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))


if __name__ == '__main__':
    unittest.main()
