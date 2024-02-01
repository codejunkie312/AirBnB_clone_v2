#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, orm


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = orm.relationship('City', backref='state',
                                  cascade='all, delete')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """ Getter for cities """
            from models import storage
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list