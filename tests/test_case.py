from Case import case

import json

app = case.app.test_client()


def test_health_check():
    response = app.get('/health-check')
    assert response.status_code == 200
    assert json.loads(response.data)["healthy"] == 'ok'


def test_v1_lower():
    response = app.post('/v1/lower',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "foo"


def test_v1_upper():
    response = app.post('/v1/upper',
                        data='{"text": "Foo"}',
                        headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert json.loads(response.data)["text"] == "FOO"
