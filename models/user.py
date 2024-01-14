#!/usr/bin/python3
"""Module for creating users"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class describes user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
