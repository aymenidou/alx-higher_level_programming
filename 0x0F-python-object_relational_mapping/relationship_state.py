#!/usr/bin/python3
"""module contain state table representation"""
from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base

# Base = declarative_base()


class State(Base):
    """state class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
