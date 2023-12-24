#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    @property
    def place_amenities(self):
        """ Getter for place_amenities"""
        from models.place import Place, place_amenity
        return relationship("Place", secondary="place_amenity",
                            back_populates="amenities")
