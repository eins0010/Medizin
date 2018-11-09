import mysql.connector
from config import DB_config

db = {
        "user": DB_config.USERNAME,
        "password": DB_config.PASSWORD,
        "database": DB_config.DATABASE,
        "raise_on_warnings": True
    }

def run_query(query):
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    cursor.execute(query)
    return [i for i in cursor]