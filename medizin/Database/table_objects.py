class UserCredentials(object):
    def __init__(self, USERID, USERNAME, E_PASSWORD):
        self.user_id = USERID
        self.username = USERNAME
        self.encrypted_password = E_PASSWORD

    def display_user(self):
        return {
                "user_id": self.user_id,
                "username": self.username,
                "password": self.encrypted_password
            }