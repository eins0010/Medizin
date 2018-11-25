from medizin.Database.table_objects import UserCredentials
from medizin.utils.common_utils import query_execution


def get_data_from_user_credentials():
    query = "select userid, username, e_password from UserCredentials"
    return execute_get_data_from_user_credentials_query(query=query)


def autheticate_user(username, password):
    query = "select username, e_password from UserCredentials where username ='{}' and e_password ='{}'".format(
        username,
        password)
    return execute_authenticate_user_query(query=query)


@query_execution
def execute_get_data_from_user_credentials_query(query, result=None):
    return [UserCredentials(*i) for i in result] if result else []


@query_execution
def execute_authenticate_user_query(query, result=None):
    return True if result else False
