from flask import request
from functools import wraps
from medizin.utils.encryption import Encryption
from config import DATABASE
from medizin.Database.connections import mssql_db, mysql_db
import pyodbc
import mysql.connector


def authenticate(func):
    @wraps(func)
    def validate_token(*args, **kwargs):
        auth_token = None
        if "Auth-Token" in request.headers:
            auth_token = request.headers["Auth-Token"]
        if not all([auth_token, Encryption.validate_user(auth_token)]):
            return {"Message": "Auth token not found or not valid"}, 401
        return func(*args, **kwargs)

    return validate_token

def query_execution(func):
    @wraps(func)
    def database_query_execution(*args, **kwargs):
        if DATABASE == "MSSQL":
            con = pyodbc.connect('Trusted_Connection=yes', **mssql_db)
            cursor = con.cursor()
            query = args[0] or kwargs["query"]
            cursor.execute(query)
            return [row for row in cursor]
        elif DATABASE == "MYSQL":
            connection = mysql.connector.connect(**mysql_db)
            cursor = connection.cursor()
            query = kwargs.get("query") or args[0]
            cursor.execute(query)
            kwargs["result"] = [i for i in cursor]
            return func(*args, **kwargs)
        else:
            return []
    return database_query_execution