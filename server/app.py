#!/usr/bin/env python3

from flask import request, session, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import app, db, api
from models import User, Recipe
from flask_migrate import Migrate
migrate = Migrate(app, db)

class Signup(Resource):
    def post(self):
        # Example implementation:
        username = request.json.get('username')
        password = request.json.get('password')
        
       
        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify(message='User created successfully'), 201
        except IntegrityError:
            return jsonify(message='Username already exists'), 422

class CheckSession(Resource):
    def get(self):
        if 'id' in session:
            user_id = session['id']
            user = User.query.get(user_id)
            if user:
                return jsonify(id=user.id, username=user.username)
        return '', 401

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['id'] = user.id
            return '', 204  # Login successful
        else:
            return '', 401  # Unauthorized

class Logout(Resource):
    def post(self):
        if 'id' in session:
            session.clear()
            return '', 204  # Logout successful
        return '', 401  # Unauthorized

class RecipeIndex(Resource):
    def get(self):
        if 'id' in session:
            user_id = session['id']
            recipes = Recipe.query.filter_by(user_id=user_id).all()
            return jsonify([recipe.serialize() for recipe in recipes])
        return '', 401  # Unauthorized

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
