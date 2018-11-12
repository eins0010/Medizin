from medizin import api, app
from flask_restplus import Resource
from medizin.MYSQL.user_credentials import get_data_from_user_credentials, autheticate_user

ns = api.namespace('Login', description='Introduction to medicine app')


@ns.route('/autheticate/<username>/<password>')
class LoginClass(Resource):
    def get(self, username, password):
        # get the Into of page
        user_credentials_list = get_data_from_user_credentials()
        return [user.display_user() for user in user_credentials_list]

    def post(self, username, password):
        result = autheticate_user(username, password)
        return "User authicated" if result else "User don't have access"
