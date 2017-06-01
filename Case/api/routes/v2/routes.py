from flask import Blueprint, request
from flask_restplus import Api, Resource, fields
from ...utils import common

blueprint = Blueprint('v2', __name__)
api = Api(blueprint)

text_payload = api.model('Resource', {
    'text': fields.String,
})


@api.route('/lower')
class Lower(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        return common.lower()


@api.route('/upper')
class Upper(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        return common.upper()


@api.route('/reverse')
class Reverse(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        content = request.get_json()
        if content is None:
            text = ''
        else:
            try:
                text = content['text'][::-1]
            except KeyError:
                text = ''
        return {'text': text}
