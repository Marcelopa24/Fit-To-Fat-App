from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('appointments').query_db(query, formulario)#regresa nuevo id del apersoan registrada
        return result

    @staticmethod
    def valida_usuario(formulario):
        # info del formulario (first_name, last_name, email, password, confirm_paswword)
        es_valido = True
        # validar que el nombre tenga 3 caracteres
        if len(formulario['first_name']) < 3:
            flash('* Nombre debe tener 3 caractres', 'registro')
            es_valido = False

        if len(formulario['last_name']) < 3:
            flash('* Apellido debe tener 3 caractres', 'registro')
            es_valido = False

        # verificar formato correcto de email, expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']):
            flash('* E-mail invalido', 'registro')
            es_valido = False

        # password con almenos 6 caracteres
        if len(formulario['password']) < 6:
            flash('* Contraseña debe tener al menos 6 caractres', 'registro')
            es_valido = False

        # password con almenos 6 caracteres
        if formulario['password'] != formulario['confirm_password']:
            flash('* Contraseñas no coinciden ', 'registro')
            es_valido = False 

        # consultar si ya existe el correo electronico en la base de datos
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('appointments').query_db(query,formulario)
        if len(results) >= 1:
            flash('* E-mail registrado previamente', 'registro')
            es_valido = False 
        
        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0])
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        user = cls(result[0])
        return user