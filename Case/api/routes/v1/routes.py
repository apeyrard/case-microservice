from flask import Blueprint, request
from flask_restplus import Api, Resource
from ...utils import common

blueprint = Blueprint('v1', __name__)
api = Api(blueprint)


@api.route('/lower')
class Lower(Resource):
    def post(self):
        return common.lower()


@api.route('/upper')
class Upper(Resource):
    def post(self):
        return common.upper()


@api.route('/reverse')
class Reverse(Resource):
    def post(self):
        content = request.get_json()
        if content is None:
            text = ''
        else:
            try:
                text = content['text'][0::-1]
            except KeyError:
                text = ''
        return {'text': text}
