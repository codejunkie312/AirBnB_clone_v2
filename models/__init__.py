#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage_type = "db"
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage_type = "fs"
storage.reload()
