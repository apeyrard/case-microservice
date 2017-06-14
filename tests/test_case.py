from Case import case

import json

app = case.app.test_client()


def test_health_check():
    response = app.get('/health-check')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))["healthy"] is True


def test_build():
    response = app.get('/build')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))["branch"]
    assert json.loads(response.data.decode('UTF-8'))["commit"]
