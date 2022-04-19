from flask_app.config.mysqlconnection import connectToMySQL


class Location:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.state = data['state']
        self.urlcode = data['urlcode']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_city(cls, data):
        query = "SELECT * FROM locations WHERE id = %(id)s"
        result = connectToMySQL('miles').query_db(query, data)
        return cls(result[0])

