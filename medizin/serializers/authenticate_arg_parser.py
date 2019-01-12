from flask_restplus import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, help='username for login', location='args')
login_parser.add_argument('password', type=str, help='password for login', location='args')