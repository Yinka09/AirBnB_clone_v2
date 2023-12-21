#!/usr/bin/python3
"""Tests city model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """Tests city model """

    def __init__(self, *args, **kwargs):
        """Public initializer """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests state_id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str  if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """Tets name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
