from flask import Blueprint
from flask_restplus import Api, Resource

import os

blueprint = Blueprint('common', __name__)
api = Api(blueprint)


@api.route('/health-check')
class HealthCheck(Resource):
    def get(self):
        return {'healthy': True}


@api.route('/build')
class Build(Resource):
    def get(self):
        return {
            'branch': os.environ['SERVICE_BRANCH'],
            'commit': os.environ['SERVICE_COMMIT']
        }
