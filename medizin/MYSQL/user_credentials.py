from medizin.MYSQL.connections import db
import mysql.connector
from medizin.MYSQL.table_objects import UserCredentials


def get_data_from_user_credentials():
    query = "select userid, username, e_password from UserCredentials"
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    cursor.execute(query)
    return [UserCredentials(*i) for i in cursor]


def autheticate_user(username, password):
    query = "select username, e_password from UserCredentials where username ='{}' and e_password ='{}'".format(username,
                                                                                                        password)
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    cursor.execute(query)
    response = [i for i in cursor]
    return True if response else False
