#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (os.environ.get("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            Get a list of all cities associated with this state.

            Returns:
                A list of City instances associated with this state.
            """

            from models import storage, City

            city_list = []

            for key in storage.all(City).values():
                if key.state_id == self.id:
                    city_list.append(key)
            return city_list
