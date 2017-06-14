from flask import Blueprint
from flask_restplus import Api, Resource, fields, reqparse

blueprint = Blueprint('v1', __name__)
api = Api(blueprint)

text_payload = api.model('Resource', {
    'text': fields.String,
})

parser = reqparse.RequestParser()
parser.add_argument('text', required=True, type=str)


@api.route('/lower')
class Lower(Resource):
    @api.marshal_with(text_payload)
    @api.expect(parser, validate=True)
    def get(self):
        text = parser.parse_args()['text']
        return {'text': text.lower()}


@api.route('/upper')
class Upper(Resource):
    @api.marshal_with(text_payload)
    @api.expect(parser, validate=True)
    def get(self):
        text = parser.parse_args()['text']
        return {'text': text.upper()}


@api.route('/reverse')
class Reverse(Resource):
    @api.marshal_with(text_payload)
    @api.expect(parser, validate=True)
    def get(self):
        text = parser.parse_args()['text']
        if text:
            return {'text': text[1::-1]}
        return {'text': ''}
