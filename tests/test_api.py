from http import HTTPStatus


def test_root_endpoint(test_client):
    response = test_client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Hello': 'World'}
