from flask import request
from functools import wraps
from medizin.utils.encryption import Encryption


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
