from medizin import api, app
from flask_restplus import Resource

ns = api.namespace('Intro', description='Introduction to medicine app')
@ns.route('/intro')
class TrainingClass(Resource):

    @ns.doc("get")
    def get(self):
        # get the Into of page
        return {
            "Medizin": "Welcome to Medizin"
        }
