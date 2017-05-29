from Case import case

import json

app = case.app.test_client()


def test_lower():
    response = app.post('/v1/lower',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "foo"


def test_upper():
    response = app.post('/v1/upper',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "FOO"


# This test is absurd, this is a feature
def test_reverse():
    response = app.post('/v1/reverse',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "F"
