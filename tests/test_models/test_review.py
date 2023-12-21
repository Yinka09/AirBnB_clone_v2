#!/usr/bin/python3
"""Tests review module """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os

class test_review(test_basemodel):
    """Tests review class """

    def __init__(self, *args, **kwargs):
        """Public initializer """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tets review place_id atrribute """
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """Tests review user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str  if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """Tests review module text attribute """
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
