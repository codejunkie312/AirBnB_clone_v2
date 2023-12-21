#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base

user, password, host, database = getenv('HBNB_MYSQL_USER'),
getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')


class DBStorage:
    """This class manages storage of hbnb models in DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class"""
        url = 'mysql+mysqldb://{}:{}@{}/{}'\
            .format(user, password, host, database)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from console import HBNBCommand

        classes = HBNBCommand.classes
        self.__session = sessionmaker(bind=self.__engine)
        new_dict = {}
        with self.__session() as session:
            if cls:
                for instance in session.query(classes[cls]).all():
                    new_dict[cls + '.' + instance.id] = instance
                return new_dict
            else:
                for key, value in classes.items():
                    for instance in session.query(value).all():
                        new_dict[key + '.' + instance.id] = instance
                return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session = sessionmaker(bind=self.__engine)
        with self.__session() as session:
            session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session = sessionmaker(bind=self.__engine)
        with self.__session() as session:
            session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        self.__session = sessionmaker(bind=self.__engine)
        with self.__session() as session:
            if obj:
                session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
