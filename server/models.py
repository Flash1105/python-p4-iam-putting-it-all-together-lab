from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class User:
    def __init__(self, username=None, password_hash=None, image_url=None, bio=None):
        self.username = username
        self.password_hash = password_hash
        self.image_url = image_url
        self.bio = bio
        self.recipes = []

    def set_password(self, password):
        # A simplified method to set the password hash for testing
        self.password_hash = password

    def check_password(self, password):
        # A simplified method to check the password hash for testing
        return self.password_hash == password

class Recipe:
    def __init__(self, title=None, instructions=None, minutes_to_complete=None):
        self.title = title
        self.instructions = instructions
        self.minutes_to_complete = minutes_to_complete
class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    minutes_to_complete = db.Column(db.Integer, nullable=False)
