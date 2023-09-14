from faker import Faker
import flask
import pytest
from random import randint, choice as rc

from app import app
from models import db, User, Recipe

app.secret_key = b'a\xdb\xd2\x13\x93\xc1\xe9\x97\xef2\xe3\x004U\xd1Z'

class TestSignup:
    '''Signup resource in app.py'''

    def test_creates_users_at_signup(self):
        '''creates user records with usernames and passwords at /signup.'''
        
        

    def test_422s_invalid_users_at_signup(self):
        '''422s invalid usernames at /signup.'''
        

class TestCheckSession:
    '''CheckSession resource in app.py'''

    def test_returns_user_json_for_active_session(self):
        '''returns JSON for the user's data if there is an active session.'''
     
    def test_401s_for_no_session(self):
        '''returns a 401 Unauthorized status code if there is no active session.'''
      
class TestLogin:
    '''Login resource in app.py'''

    def test_logs_in(self):
        '''logs users in with a username and password at /login.'''
        
       
    def test_401s_bad_logins(self):
        '''returns 401 for an invalid username and password at /login.'''
        
    def test_logs_out(self):
        '''logs users out at /logout.'''
       
    def test_401s_if_no_session(self):
        '''returns 401 if a user attempts to logout without a session at /logout.'''
       

class TestRecipeIndex:
    '''RecipeIndex resource in app.py'''

    def test_lists_recipes_with_200(self):
        '''returns a list of recipes associated with the logged in user and a 200 status code.'''

       
    def test_get_route_returns_401_when_not_logged_in(self):
        
      
        # start actual test here
        with app.test_client() as client:

            with client.session_transaction() as session:
                
                session['user_id'] = None

            response = client.get('/recipes')
            

    def test_creates_recipes_with_201(self):
        '''returns a list of recipes associated with the logged in user and a 200 status code.'''

    def test_returns_422_for_invalid_recipes(self):
      
        # start actual test here
        with app.test_client() as client:

            with client.session_transaction() as session:
                
                session
            fake = Faker()