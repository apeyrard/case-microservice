from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/health-check')
def health_check():
    return jsonify({'healthy': True})


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
