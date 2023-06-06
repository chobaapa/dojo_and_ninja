from flask_app.config.mysqlconnection import connectToMySQL
from .models_ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
    
    # @classmethod
    # def get_one_with_ninjas(cls, data):
    #     query = *SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojo.id = %(id)s;*
    #     results = connecttomysql('dojo_and_ninjas').query_db(query,data)
    #     print(results)
    #     dojo = cls(results[0])
    #     from row in results:
    #         n = {
    #             'id': row['ninjas.id'],
    #             'first_name': row['ninjas.id'],
    #             'last_name': row['ninjas.id'],
    #             'age': row['ninjas.id'],
    #             'created_at': row['ninjas.id'],
    #             'updated_at': row['ninjas.id'],
    #             }
    #     dojo.ninjas.append( Ninja(n))
    # return Dojo