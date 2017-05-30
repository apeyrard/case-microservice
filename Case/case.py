from flask import Flask, request

import os

from .api.routes.common_routes import api as api_common
from .api.routes.v1.routes import api as api_v1
from .api.routes.v2.routes import api as api_v2

import logging
from pythonjsonlogger import jsonlogger


# Creating and configuring logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)


formatter = jsonlogger.JsonFormatter("%(asctime)s - %(levelname)s - "
                                     "%(filename)s - %(funcName)s - %(lineno)s"
                                     "- %(module)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)

# use loggerAdapter to add commit and branch
extra = {
    "Branch": os.environ["SERVICE_BRANCH"],
    "Commit": os.environ["SERVICE_COMMIT"]
}
logger = logging.LoggerAdapter(logger, extra)


app = Flask(__name__)
logger.warning("App started", extra={'foo': 'bar'})

# Registering blueprints for different versions of api
app.register_blueprint(api_common)
app.register_blueprint(api_v1, url_prefix='/v1')
app.register_blueprint(api_v2, url_prefix='/v2')


# Log received requests
@app.before_request
def log_request():
    debug_data = {
            'form': request.form,
            'args': request.args,
            'values': request.values,
            'cookies': request.cookies,
            'headers': request.headers,
            'data': request.data,
            'files': request.files,
            'environ': request.environ,
            'method': request.method,
            'url': request.url,
            'blueprint': request.blueprint,
            'endpoint': request.endpoint
    }
    info_data = {
            'form': request.form,
            'args': request.args,
            'values': request.values,
            'cookies': request.cookies,
            'headers': request.headers,
            'data': request.data,
            'files': request.files,
            'method': request.method,
            'url': request.url,
            'blueprint': request.blueprint,
            'endpoint': request.endpoint
    }
    logger.debug('Request received', extra={'request': debug_data})
    logger.info('Request received', extra={'request': info_data})


# Set headers in after_request hook
@app.after_request
def set_headers(response):
    response.headers["Service-Branch"] = os.environ["SERVICE_BRANCH"]
    response.headers["Service-Commit"] = os.environ["SERVICE_COMMIT"]
    return response
