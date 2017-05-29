from Case import case

import json

app = case.app.test_client()


def test_lower():
    response = app.post('/v2/lower',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "foo"


def test_upper():
    response = app.post('/v2/upper',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "FOO"


def test_reverse():
    response = app.post('/v2/reverse',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "ooF"
