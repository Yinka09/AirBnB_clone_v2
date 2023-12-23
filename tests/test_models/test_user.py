#!/usr/bin/python3
"""Tests user module """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from models.base_model import Base, BaseModel
import unittest
import MySQLdb
from datetime import datetime


class test_User(test_basemodel):
    """Tests user module """

    def __init__(self, *args, **kwargs):
        """Public initializer """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests user firstname """
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_last_name(self):
        """Tests user last_name """
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """Tests email """
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """Tets user passsword """
        new = self.value()
        self.assertEqual(type(new.password), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
    
    def test_str(self):
        """Test __str__ representation."""
        s = self.user.__str__()
        self.assertIn("[User] ({})".format(self.user.id), s)
        self.assertIn("'id': '{}'".format(self.user.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.user.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.user.updated_at)), s)
        self.assertIn("'email': '{}'".format(self.user.email), s)
        self.assertIn("'password': '{}'".format(self.user.password), s)

     @unittest.skipIf(type(models.storage) == DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        old = self.user.updated_at
        self.user.save()
        self.assertLess(old, self.user.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("User." + self.user.id, f.read())

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_save_dbstorage(self):
        """Test save method with DBStorage."""
        old = self.user.updated_at
        self.user.save()
        self.assertLess(old, self.user.updated_at)
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * \
                          FROM `users` \
                         WHERE BINARY email = '{}'".
                       format(self.user.email))
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(self.user.id, query[0][0])
        cursor.close()

    def test_to_dict(self):
        """Test to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(dict, type(user_dict))
        self.assertEqual(self.user.id, user_dict["id"])
        self.assertEqual("User", user_dict["__class__"])
        self.assertEqual(self.user.created_at.isoformat(),
                         user_dict["created_at"])
        self.assertEqual(self.user.updated_at.isoformat(),
                         user_dict["updated_at"])
        self.assertEqual(self.user.email, user_dict["email"])
        self.assertEqual(self.user.password, user_dict["password"])
