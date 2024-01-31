#!/usr/bin/python3
"""This module defines a class User"""
import models
import bcrypt
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.storage_type == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    
    def __init__(self, *args, **kwargs):
        """constructor"""
        if "password" in kwargs:
            password = kwargs["password"]
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(password.encode(), salt)
            kwargs["password"] = password
        super().__init__(*args, **kwargs)
