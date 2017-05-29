from flask import Flask, request, jsonify

import logging
from logging.config import fileConfig


fileConfig("logging.conf")
logger = logging.getLogger(__name__)

app = Flask(__name__)
logger.warning("App started", extra={'foo': 'bar'})


@app.route('/health-check')
def health_check():
    return jsonify({'healthy': true})


@app.route('/v1/upper', methods=['POST'])
def upper():
    content = request.get_json()
    if content is None:
        text = ''
    else:
        try:
            text = content['text'].upper()
        except AttributeError:
            text = ''
    return jsonify({'text': text})


@app.route('/v1/lower', methods=['POST'])
def lower():
    content = request.get_json()
    if content is None:
        text = ''
    else:
        try:
            text = content['text'].lower()
        except AttributeError:
            text = ''
    return jsonify({'text': text})


if __name__ == "__main__":
    app.run(port=5001, debug=True)
