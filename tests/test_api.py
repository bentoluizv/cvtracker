from http import HTTPStatus


def test_root_endpoint(test_client):
    response = test_client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_api_index_endpoint(test_client):
    response = test_client.get('/api/v1')
    assert response.status_code == HTTPStatus.OK
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() == {
        'description': 'API para o aplicativo TrackerCV',
        'version': '1.0.0',
        'api': '/api/v1',
        'docs': '/docs',
        'redoc': '/redoc',
        'env': 'development',
    }
