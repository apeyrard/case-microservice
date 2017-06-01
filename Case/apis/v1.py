from flask import Blueprint
from flask_restplus import Api, Resource, fields
from ..core.utils import case_utils

blueprint = Blueprint('v1', __name__)
api = Api(blueprint)

text_payload = api.model('Resource', {
    'text': fields.String,
})


@api.route('/lower')
class Lower(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        return case_utils.lower()


@api.route('/upper')
class Upper(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        return case_utils.upper()


@api.route('/reverse')
class Reverse(Resource):
    @api.expect(text_payload, validate=True)
    def post(self):
        try:
            text = api.payload["text"]
        except KeyError:
            return {'text': ''}
        if text:
            return {'text': text[1::-1]}
        return {'text': ''}
