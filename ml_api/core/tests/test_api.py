import ml_api.core.services

def test_get(client):
    r = client.get('/api/')
    assert r.json() == dict(hello="world")


def test_post(client, values, mocker):
    # mocker.patch.object(ml_api.core.services, 'predict', return_value=20.0)
    r = client.post('/api/', data=values, content_type='aplication/json')
    assert 'predict' in r.json()
    assert r.json() == dict(predict=20.0)