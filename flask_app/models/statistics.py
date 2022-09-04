from email.mime.application import MIMEApplication
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Statistic:

    def __init__(self, data):
        self.id = data['id']
        self.height = data['height']
        self.weight = data['weight']
        self.month = data['month']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO appointments.statistics (height,weight,month,user_id) VALUES (%(height)s, %(weight)s,%(month)s,%(user_id)s) ;"
        result = connectToMySQL('appointments').query_db(query, data)
        print(result)
        return result
        

    @classmethod
    def show_all(cls, data):
        query = "SELECT * FROM statistics join users on users.id = statistics.user_id where users.id = %(id)s;"
        results = connectToMySQL('appointments').query_db(query, data)  # Lista de diccionarios
        statistics = []
        for x in results:
            statistics.append(cls(x))

        return statistics

    @classmethod
    def get_statistic(cls, data):
        query = "select * from statistics where id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE statistics SET height=%(height)s, weight=%(weight)s, month=%(month)s, user_id=%(user_id)s where id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, data)
        return result

    @classmethod
    def delete(cls, formulario):  # Recibe formulario con id de receta a borrar
        query = "DELETE FROM statistics WHERE id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        return result
    
