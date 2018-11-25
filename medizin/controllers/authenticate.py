from medizin import api
from flask_restplus import Resource
from medizin.Database.tables_queries import get_data_from_user_credentials, autheticate_user
from medizin.utils.encryption import Encryption
from medizin.utils.common_utils import authenticate


ns = api.namespace('Login', description='Introduction to medicine app')


@ns.route('/authenticate/<username>/<password>')
class LoginClass(Resource):
    def post(self, username, password):
        result = autheticate_user(username, password)
        if result:
            user_auth_token = Encryption.generate_RSA_token(username, password)
            return {"user": username,
                    "auth_token": user_auth_token
                    }
        else:
            return {"user": username,
                    "authentication": "User is not authorised to use this service"
                    }

@ns.route('UserDetails')
@ns.header("Auth-Token")
class User(Resource):
    @authenticate
    def get(self):
        # get the Into of page
        user_credentials_list = get_data_from_user_credentials()
        return [user.display_user() for user in user_credentials_list]