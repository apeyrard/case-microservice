from flask import request


def upper():
    content = request.get_json()
    if content is None:
        text = ''
    else:
        try:
            text = content['text'].upper()
        except KeyError:
            text = ''
    return {'text': text}


def lower():
    content = request.get_json()
    if content is None:
        text = ''
    else:
        try:
            text = content['text'].lower()
        except KeyError:
            text = ''
    return {'text': text}
