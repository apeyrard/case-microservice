from flask import Flask, request

import os

from .apis.common_routes import blueprint as api_common
from .apis.v1 import blueprint as api_v1
from .apis.v2 import blueprint as api_v2

from raven.contrib.flask import Sentry

import logging
from pythonjsonlogger import jsonlogger


# Creating and configuring logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# use filter to add commit and branch
class AppFilter(logging.Filter):
    def filter(self, record):
        record.branch = os.environ["SERVICE_BRANCH"]
        record.commit = os.environ["SERVICE_COMMIT"]
        return True


logger.addFilter(AppFilter())

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)


formatter = jsonlogger.JsonFormatter("%(asctime)s - %(levelname)s - %(branch)s"
                                     " - %(commit)s - %(filename)s"
                                     " - %(funcName)s - %(lineno)s"
                                     " - %(module)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


app = Flask(__name__)
app.register_blueprint(api_common)
app.register_blueprint(api_v1, url_prefix='/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')

# Configuring Sentry
sentry = Sentry(app)


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
