#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class for DB"""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')

else:
    class State(Basemodel):
        """State class for FS"""

       @property
       def cities(self):
           """Returns the list of City instances"""
           return[city
                  for city in storage.all(City).values()
                  if city.state_id == self.id]


