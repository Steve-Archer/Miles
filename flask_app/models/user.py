from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.score = data['score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (name, score) VALUES (%(name)s, '20000')"
        connectToMySQL('miles').query_db(query, data)
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE name = %(name)s"
        result = connectToMySQL('miles').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    @classmethod
    def static_get_user(cls, data):
        query = "SELECT * FROM users WHERE name = %(name)s"
        result = connectToMySQL('miles').query_db(query, data)
        if len(result) < 1:
            return False
        return True
    @classmethod
    def get_score(cls,data):
        query = "SELECT score FROM users WHERE name = %(name)s"
        result = connectToMySQL('miles').query_db(query, data)
        return result
    @classmethod
    def new_score(cls, data):
        query = "UPDATE users Set score = %(score)s WHERE name = %(name)s"
        connectToMySQL('miles').query_db(query, data)
    @classmethod
    def get_best_scores(cls):
        query = "SELECT * FROM users ORDER BY score;"
        result = connectToMySQL('miles').query_db(query)
        return result
    @staticmethod
    def validate_user(user):
        is_valid = True
        if User.static_get_user(user):
            is_valid = False
            flash('Name is already taken. Try another name')
        if len(user['name']) < 1:
            is_valid = False
            flash('Name required to Play!')
        if len(user['name']) > 30:
            is_valid = False
            flash('name must be 30 characters or less')
        return is_valid


