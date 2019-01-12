from medizin import api
from flask_restplus import fields

LoginModel = api.model('LoginModel', {
    "username": fields.String,
    "user_id": fields.String,
    "encrypted_password": fields.String
})
