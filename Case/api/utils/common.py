from flask import request, jsonify


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
