from medizin.utils.rsa_encryption import RSAEncryption
import time


class Encryption(object):
    user_auth_token = None
    RSA_keys = RSAEncryption().get_encrypt_and_decipher_keys()
    RSA_user_map = {}  # {encrypt_password: decipher_password}
    alphabet_key_mapping = {key: index + 1 for index, key in enumerate(
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^*()-_=+0123456789"))}
    alphabet_value_mapping = {index + 1: key for index, key in enumerate(
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^*()-_=+0123456789"))}

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
    def alphabet_index_reverse_order_mapping(cls, value):
        length = len(cls.alphabet_value_mapping.keys())
        if value > length:
            value = value % length
        return cls.alphabet_value_mapping[value]

    @classmethod
    def generate_RSA_token(cls, username, password):
        input_text = username + password
        if isinstance(cls.RSA_keys, dict):
            return cls.RSA_keys
        else:
            encrypted_password = "".join([cls.alphabet_index_reverse_order_mapping(
                pow(cls.alphabet_key_mapping[each_char],
                    cls.RSA_keys.lock_key) % cls.RSA_keys.mod_key) for each_char in
                input_text])
            cls.user_auth_token = encrypted_password
            decipher_password = "".join([cls.alphabet_index_reverse_order_mapping(
                pow(cls.alphabet_key_mapping[each_char],
                    cls.RSA_keys.unlock_key) % cls.RSA_keys.mod_key) for each_char in
                encrypted_password])
            cls.RSA_user_map[encrypted_password] = decipher_password
            return "&".join(
                [str(time.time()), encrypted_password, str(cls.RSA_keys.unlock_key), str(cls.RSA_keys.mod_key)])

    @classmethod
    def validate_user(cls, user_auth_token):
        if user_auth_token:
            initialed_time, auth_token, decipher_key, mod_key = user_auth_token.split("&")
            decipher_password = "".join([cls.alphabet_index_reverse_order_mapping(
                pow(cls.alphabet_key_mapping[each_char],
                    cls.RSA_keys.lock_key) % cls.RSA_keys.mod_key) for each_char in
                auth_token])
            if cls.RSA_user_map[auth_token] == decipher_password and time.time() - float(initialed_time) <= 1800:
                # Here 1800 means expiry time set to 30 minutes
                return True
        return False
