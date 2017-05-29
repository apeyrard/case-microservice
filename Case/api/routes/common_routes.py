from flask import Blueprint, jsonify

import os

api = Blueprint('common', __name__)


@api.route('/health-check')
def health_check():
    return jsonify({'healthy': True})


@api.route('/build')
def build():
    return jsonify({'branch': os.environ['SERVICE_BRANCH'],
                    'commit': os.environ['SERVICE_COMMIT']})
