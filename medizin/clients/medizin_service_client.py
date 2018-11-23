from flask import request


class MedizinServiceClient(object):
    @staticmethod
    def get_headers(content_type='application/json'):
        headers = {}
        if content_type:
            headers["Content-type"] = content_type
            headers["Auth-Token"] = request.headers['Auth-Token']
        return headers
