#!/usr/bin/python3
"""This module instatiates FileStorage class"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
