class Encryption(object):
    user_auth_token = None

    @staticmethod
    def encryption(password):
        # Encryption algorithm is defined as follows
        # Convert each character of password to its corresponding ascii values and join them
        encrypted_password = "".join([str(ord(each_char)) for each_char in password])
        return encrypted_password

    @classmethod
    def auth_token(cls, username, password):
        # Encryption algorithm is defined as follows
        # Convert each character of username and password to its corresponding ascii values and join them
        encrypted_password = "".join([str(ord(each_char)) for each_char in password + username])
        cls.user_auth_token = encrypted_password
        return encrypted_password

    @classmethod
    def validate_user(cls, user_auth_token):
        if user_auth_token and cls.user_auth_token == user_auth_token:
            return True
        return False
