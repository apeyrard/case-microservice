from flask import Blueprint, jsonify

api = Blueprint('common', __name__)


@api.route('/health-check')
def health_check():
    return jsonify({'healthy': True})
