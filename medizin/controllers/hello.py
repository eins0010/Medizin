from medizin import api, app
from flask_restplus import Resource
from medizin.MYSQL.connections import run_query

ns = api.namespace('Intro', description='Introduction to medicine app')
@ns.route('/intro')
class TrainingClass(Resource):

    @ns.doc("get")
    def get(self):
        # get the Into of page
        query = "select * from test"
        return run_query(query)
