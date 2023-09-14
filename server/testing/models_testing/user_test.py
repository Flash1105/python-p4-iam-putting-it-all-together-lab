from sqlalchemy.exc import IntegrityError
import pytest

from app import app
from models import db, User, Recipe

class TestUser:
    '''User in models.py'''

    def test_has_attributes(self):
        '''has attributes username, _password_hash, image_url, and bio.'''
        
    def test_requires_username(self):
        '''requires each record to have a username.'''

       

    def test_requires_unique_username(self):
        '''requires each record to have a username.'''

       

    def test_has_list_of_recipes(self):
        '''has records with lists of recipes records attached.'''

       

        

            