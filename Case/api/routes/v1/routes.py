from flask import Blueprint, request, jsonify
from ...utils import common

api = Blueprint('v1', __name__)


@api.route('/lower', methods=['POST'])
def lower():
    return common.lower()


@api.route('/upper', methods=['POST'])
def upper():
    return common.upper()


@api.route('/reverse', methods=['POST'])
def reverse():
    content = request.get_json()
    if content is None:
        text = ''
    else:
        try:
            text = content['text'][0::-1]
        except AttributeError:
            text = ''
    return jsonify({'text': text})
