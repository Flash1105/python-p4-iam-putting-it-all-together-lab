import pytest
from sqlalchemy.exc import IntegrityError

from app import app
from models import db, Recipe

class TestRecipe:
    '''User in models.py'''

    def test_has_attributes(self):
        '''has attributes title, instructions, and minutes_to_complete.'''
        
    def test_requires_title(self):
        '''requires each record to have a title.'''

    
         

    def test_requires_50_plus_char_instructions(self):
        with app.app_context():

            Recipe.query.delete()
            db.session.commit()

            recipe = Recipe(
                title="Generic Ham",
                instructions="idk lol")

        

