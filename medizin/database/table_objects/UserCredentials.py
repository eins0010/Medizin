from collections import OrderedDict
from medizin.utils.common_utils import query_execution


class UserCredentials(object):
    def __init__(self, USERID, USERNAME, E_PASSWORD):
        self.user_id = USERID
        self.username = USERNAME
        self.encrypted_password = E_PASSWORD

    def __str__(self):
        return OrderedDict({
            "user_id": self.user_id,
            "username": self.username,
            "encrypted_password": self.encrypted_password
        })

    @staticmethod
    def get_data_from_user_credentials():
        query = "select userid, username, e_password from UserCredentials"
        return UserCredentials.execute_get_data_from_user_credentials_query(query=query)

    @staticmethod
    @query_execution
    def execute_get_data_from_user_credentials_query(query, result=None):
        return [UserCredentials(*i) for i in result] if result else []

# The below two methods can be moved later based on Data Design Model
def autheticate_user(username, password):
    query = "select username, e_password from UserCredentials where username ='{}' and e_password ='{}'".format(
        username,
        password)
    return execute_authenticate_user_query(query=query)


@query_execution
def execute_authenticate_user_query(query, result=None):
    return True if result else False
