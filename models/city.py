#!/usr/bin/python3
"""Module for creating cities"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""  # it will be the State.id
    name = ""
