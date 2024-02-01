#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

user, password, host, database = (getenv('HBNB_MYSQL_USER'),
                                  getenv('HBNB_MYSQL_PWD'),
                                  getenv('HBNB_MYSQL_HOST'),
                                  getenv('HBNB_MYSQL_DB'))


class DBStorage:
    """This class manages storage of hbnb models in DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class"""
        url = 'mysql+mysqldb://{}:{}@{}:3306/{}'\
            .format(user, password, host, database)
        self.__engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from console import classes

        new_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                class_str = classes[c]
                print(class_str)
                objs = self.__session.query(classes[c]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()
