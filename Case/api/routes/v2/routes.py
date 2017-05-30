from flask import Blueprint, request, jsonify
from ...utils import common

api = Blueprint('v2', __name__)


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
            text = content['text'][::-1]
        except KeyError:
            text = ''
    return jsonify({'text': text})
