from medizin import api
from flask_restplus import Resource
from medizin.database.table_objects.UserCredentials import UserCredentials, autheticate_user
from medizin.utils.encryption import Encryption
from medizin.utils.common_utils import authenticate
from medizin.serializers.authenticate_model import LoginModel
from medizin.serializers.authenticate_arg_parser import login_parser
from operator import itemgetter

ns = api.namespace('Login', description='Introduction to medicine app')


@ns.route('/authenticate')
class LoginClass(Resource):
    @ns.expect(login_parser)
    def post(self):
        kwargs = login_parser.parse_args()
        username, password = itemgetter("username", "password")(kwargs)
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


@ns.route('/UserDetails')
@ns.header("Auth-Token")
class User(Resource):
    @authenticate
    @ns.marshal_with(LoginModel)
    def get(self):
        # get the Into of page
        return UserCredentials.get_data_from_user_credentials()
