#!/usr/bin/python3
"""Test for user"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))


if __name__ == '__main__':
    unittest.main()
