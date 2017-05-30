from Case import case

import json

app = case.app.test_client()


def test_lower():
    response = app.post('/v1/lower',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "foo"
    response = app.post('/v1/lower',
                        data='{}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""
    response = app.post('/v1/lower',
                        data='{"bar": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""


def test_upper():
    response = app.post('/v1/upper',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "FOO"
    response = app.post('/v1/upper',
                        data='{}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""
    response = app.post('/v1/upper',
                        data='{"bar": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""


# This test is absurd, this is a feature
def test_reverse():
    response = app.post('/v1/reverse',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "F"
    response = app.post('/v1/reverse',
                        data='{}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""
    response = app.post('/v1/reverse',
                        data='{"foo": "bar"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == ""
