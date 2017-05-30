from flask import Flask

import os

from .api.routes.common_routes import api as api_common
from .api.routes.v1.routes import api as api_v1
from .api.routes.v2.routes import api as api_v2

import logging
from logging.config import fileConfig


fileConfig("logging.conf")
logger = logging.getLogger(__name__)

app = Flask(__name__)
logger.warning("App started", extra={'foo': 'bar'})

# Registering blueprints for different versions of api
app.register_blueprint(api_common)
app.register_blueprint(api_v1, url_prefix='/v1')
app.register_blueprint(api_v2, url_prefix='/v2')


# Set headers in after_request hook
@app.after_request
def set_headers(response):
    response.headers["Service-Branch"] = os.environ["SERVICE_BRANCH"]
    response.headers["Service-Commit"] = os.environ["SERVICE_COMMIT"]
    return response
