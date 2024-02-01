#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


if models.storage_type == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id', ondelete='CASCADE',
                       onupdate='CASCADE'),
            primary_key=True),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id',
                       ondelete='CASCADE',
                       onupdate='CASCADE'),
            primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False,
                                 backref="place_amenities")
        reviews = relationship("Review", backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def reviews(self):
            """Getter for reviews"""
            from models import storage
            from models.review import Review
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter for amenities"""
            from models import storage
            from models.amenity import Amenity
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list
