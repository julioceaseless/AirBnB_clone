#!/usr/bin/python3
"""Test for State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """
    def test_instance_creation(self):
        """ """
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """ """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """ """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))


if __name__ == '__main__':
    unittest.main()
