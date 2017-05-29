from Case import case

import json

app = case.app.test_client()


def test_health_check():
    response = app.get('/health-check')
    assert response.status_code == 200
    assert json.loads(response.data)["healthy"] is True
