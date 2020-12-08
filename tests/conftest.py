import pytest
from rekrutacja import create_app


@pytest.fixture
def app():

    app = create_app({
        'ENV': 'developement',
        'TESTING': True,
    })

    app.test_cli_runner().invoke(args=['init-db', '--clear', '--src=test-db'])

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions():
    def __init__(self, client):
        self._client = client

    def token(self, login='Kate', password='Kate'):
        return self._client.post(
            '/auth/token',
            json={'login': login, 'password': password}
        ).json['token']


@pytest.fixture
def auth(client):
    return AuthActions(client)
