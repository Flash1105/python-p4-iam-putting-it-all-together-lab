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

        with app.app_context():

            db.session.commit()

            user = User()
            db.session.commit()

    def test_requires_unique_username(self):
        '''requires each record to have a username.'''

       

    def test_has_list_of_recipes(self):
        '''has records with lists of recipes records attached.'''

        with app.app_context():

            db.session.commit()

            user = User(username="Prabhdip")

            recipe_1 = Recipe(
                title="Delicious Shed Ham",
                instructions="""Or kind rest bred with am shed then. In""" + \
                    """ raptures building an bringing be. Elderly is detract""" + \
                    """ tedious assured private so to visited. Do travelling""" + \
                    """ companions contrasted it. Mistress strongly remember""" + \
                    """ up to. Ham him compass you proceed calling detract.""" + \
                    """ Better of always missed we person mr. September""" + \
                    """ smallness northward situation few her certainty""" + \
                    """ something.""",
                minutes_to_complete=60,
                )
            recipe_2 = Recipe(
                title="Hasty Party Ham",
                instructions="""As am hastily invited settled at limited""" + \
                             """ civilly fortune me. Really spring in extent""" + \
                             """ an by. Judge but built gay party world. Of""" + \
                             """ so am he remember although required. Bachelor""" + \
                             """ unpacked be advanced at. Confined in declared""" + \
                             """ marianne is vicinity.""",
                minutes_to_complete=30,
                )

            user.recipes.append(recipe_1)
            user.recipes.append(recipe_2)

            db.session.commit()

            