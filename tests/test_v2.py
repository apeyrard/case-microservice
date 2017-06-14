from Case import case

import json

app = case.app.test_client()


def test_lower():
    response = app.get('/api/v2/lower?text=Foo')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))["text"] == "foo"


def test_upper():
    response = app.get('/api/v2/upper?text=Foo')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))["text"] == "FOO"


# This test is absurd, this is a feature
def test_reverse():
    response = app.get('/api/v2/reverse?text=Foo')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))["text"] == "ooF"
